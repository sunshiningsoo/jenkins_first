pipeline {    
    agent { docker { image 'bitnami/pytorch:latest' } }
    stages {
        stage('build') {
            steps {
                sh 'pip3 install flask parameterized'
            }
        }

        // 새로운 스테이지를 추가했습니다. exit(0), 즉 성공한 스테이지로 만듭니다.
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