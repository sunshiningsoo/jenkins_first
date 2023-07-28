pipeline {
	// section : agent
	// docker agent를 사용합니다. 이때 사용하는 도커 이미지는 python:3.11.4-alpine입니다.
    agent { docker { image 'python:3.11.4-alpine' } }
    
    // section : stages
    // 하나의 stage를 가진 간단한 파이프라인입니다.
    stages {
    	// 'build' stage를 시작합니다.
        stage('build') {
        	// python 버전을 출력합니다.
            steps {
                sh 'python --version'
            }
        }
    }
     
    // section : post
    // stage가 종료된 후에 조건에 따라 실행됩니다.
    post{
    	// always는 성공, 실패 여부와 무관하게 실행됩니다.
        always {
            echo "Always, success or not"
        }
    }
}
