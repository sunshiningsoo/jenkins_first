pipeline {
    agent any
    stages {
        stage('TestTrain') {
            steps {
                // 유닛 테스트 실행
                sh 'cd train'
                sh 'python3 -m unittest train_test.py'
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
