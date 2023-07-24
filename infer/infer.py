import os
import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision.transforms import transforms
from torchvision.datasets import ImageFolder
from PIL import Image
from io import BytesIO
import requests


from flask import Flask, request, jsonify
import sys

def init():
    lib_path = os.environ.get('LIBPATH')
    global model
    if lib_path is None:
        lib_path = '../lib/'

    sys.path.append(lib_path)
    from digit_recognizer import DigitRecognizer
    model = DigitRecognizer()

    model_path = os.environ.get('MODELPATH')    
    if model_path is None:                      
        model_path = '../model/'                

    model_url = os.environ.get("MODELURL")
    if model_url is None:
        model_url = "http://localhost:5002/model"
    try:
        response = requests.get(model_url)
        if response.status_code == 200:
            model_bytes = response.content
        else:
            print('Failed to download model file.')
            exit(-1)
        model.load_state_dict(torch.load(BytesIO(model_bytes)))
    except Exception as e:
        print('Failed to load model from redis')
        try:
            model.load_state_dict(torch.load(model_path + 'modelfile')) #3
        except Exception as e:
            print('Failed to load model from file')
            exit(-1)

    model.eval()

def infer(image_file):
    try:
        transform = transforms.Compose([transforms.Grayscale(), transforms.ToTensor()])

        image = Image.open(image_file).convert('L')     
        image = transform(image).unsqueeze(0)           

        # 추론
        with torch.no_grad():                           
            output = model(image)                       

        # 결과 출력
        _, predicted = torch.max(output, 1)             
        return None, predicted.item()
    except Exception as e:                              
        return e, -1

init()
app = Flask(__name__)                   
app.debug = True                        



@app.route('/recognize', methods=['POST'])          
def recog_image():                                  
    if 'image' not in request.files:                
        return "No image file uploaded", 400        
    image_file = request.files['image']             
    e, result = infer(image_file)
    if e == None:
        return jsonify({'result':result})     
    else:
        return f"Error recognizing image: {str(e)}", 500



if __name__ == '__main__':      
    app.run(host='0.0.0.0', port=5001)                   
