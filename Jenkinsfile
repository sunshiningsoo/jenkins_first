pipeline {
    agent { docker { image 'python:3.11.4-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('success_stage') {
            steps {
                sh 'echo "exit(0)" > s; python3 s'
            }
        }
        stage('failure_stage') {
            steps {
                sh 'echo "exit(1)" > f; python3 f'
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