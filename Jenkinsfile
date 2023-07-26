pipeline {

    agent any

    stages {


        stage('UnitTest') {
            steps {
                // 유닛 테스트 실행
                sh '''cd train
                pwd
                '''
                sh 'python3 -m unittest train/train_test.py'
            }
        }

        stage('DockerBuildAndPush') {
            steps {
                // 도커 이미지 빌드
                script {
                    def dockerImage = docker.build("jenkinstest:0")
                }

                // 도커 허브에 푸시
//                withDockerRegistry([credentialsId: "your-dockerhub-credentials", url: "https://index.docker.io/v1/"]) {
//                    dockerImage.push()
//                }
            }
        }
    }

    post {
        // 유닛 테스트가 실패하면 알림
        failure {
            mail to: 'your-email@example.com', subject: 'Unit Test Failed', body: "Build #${env.BUILD_NUMBER} failed due to unit test failures."
        }
    }
}
