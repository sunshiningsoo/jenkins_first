pipeline {    
    agent { docker { image 'pythonxxx:3.11.4-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        // 새로운 스테이지를 추가했습니다. exit(1), 즉 실패한 스테이지를 만듭니다.
        stage('failure_stage') {
            steps {
                sh 'echo "exit(1)" > f.py; python3 f.py'
            }
        }
        // 새로운 스테이지를 추가했습니다. exit(0), 즉 성공한 스테이지로 만듭니다.
        stage('success_stage') {
            steps {
                sh 'echo "exit(0)" > s.py; python3 s.py'
            }
        }

    }    
    post{
        // success, failure, aborted를 추가하였습니다.
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