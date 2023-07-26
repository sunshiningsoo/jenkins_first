pipeline {
    // bitnami/pytorch 이미지를 사용합니다.    
    agent none
    stages {        
        // Test stage에서는 테스트 환경을 만들고 unittest를 수행합니다.
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

        // BuildImage stage에서는 도커 이미지를 생성합니다.
        stage('BuildImage') {
            agent { node {label 'docker_build' } }           
            steps {
                script {
                    def trainImage = docker.build("trainimage:0", "-f ./Dockerfile.train .")
                    def inferImage = docker.build("inferimage:0", "-f ./Dockerfile.infer .")
                }
            }
        }

        // TestDeploy stage에서는 도커 서비스를 배포합니다.
        stage('TestDeploy') {
            agent { node {label 'docker_build' } }           
            steps {
                sh'''
                    if docker service ls --format '{{.Name}}' | grep -q inferservice; then
                        # 도커 스웜 서비스 업데이트
                        docker service update --image inferimage:0 --update-parallelism 1 --update-delay 10s inferservice
                    else
                        # 도커 스웜 서비스 생성
                        docker service create -t --mount type=bind,source=./model,target=/model -p 5001:5001 --replicas=3 --name inferservice inferimage:0
                    fi
                '''
            }
        }
    }
    post {
        failure {
            echo "Fail"
        }
        success {
            echo "Success"
        }
    }
}
