pipeline {
    // bitnami/pytorch 이미지를 사용합니다.    
    agent { 
        docker { 
            image 'bitnami/pytorch:latest' 
            args '-u 1001:0'
        } 
    }
    stages {
        // build stage에서는 flask와 parameterized 패키지를 설치합니다.
        stage('Setup') {
            steps {
                sh 'pip3 install flask parameterized'
            }
        }

        // test stage에서는 unittest를 진행합니다.
        stage('Test') {
            steps {
                sh'''
                    cd train
                    python3 -m unittest train_test.py
                '''
                sh '''
                    cd infer
                    python3 infer_test.py
                '''
            }
        }
        stage('BuildImage') {
            agent { node 'Built-In Node' }            
            steps {
                script {
                    def dockerImage = docker.build("trainimage:0", "-f ./Dockerfile.train .")
                }
            }
        }
    }
    post {
        // 유닛 테스트가 실패
        failure {
            echo "Fail"
        }
        // 유닛 테스트가 성공
        success {
            echo "Success"
        }
    }
}
