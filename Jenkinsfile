pipeline {
    agent none
    stages {        
        // Test stage에서는 테스트 환경을 만들고 unittest를 수행합니다.
        // Test 환경은 bitnami/pytorch로 만든 컨테이너에 패키지를 추가 설치합니다.
        stage('Test') {
            agent { 
                docker { 
                    image 'bitnami/pytorch:latest' 
                    args '-u 1001:0'
                }
            } 
            
            steps {
                sh 'pip3 install flask parameterized'
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
