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
        stage('build') {
            steps {
                sh 'pip3 install flask parameterized'
            }
        }

        // test stage에서는 unittest를 진행합니다.
        stage('test') {
            steps {
                sh' cd train'
                sh 'python3 -m unittest train_test.py'
                sh 'cd ../infer'
                sh 'python3 infer_Test.py'
            }
        }
    }    
    post{
        success {
            echo "Only success"
        }
        failure {
            echo "Only failure"
        }
        aborted {
            echo "Only aborted"
        }        
        always {
            echo "Always, success or not"
        }
    }
}