pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo Building Banking System'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Testing Banking System'
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Deploying Banking System'
            }
        }
    }

    post {
        success {
            echo 'Build Successful'
        }
    }
}
