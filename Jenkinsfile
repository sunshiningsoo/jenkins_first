pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
    post{
        always {
            echo "Hello, this is message in post section and always excuted,  success or not."
        }
    }
}