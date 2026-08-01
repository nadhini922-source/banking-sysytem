<<<<<<< HEAD
pipeline {
    agent any

    stages {
        stage('Hello World') {
            steps {
                bat 'python hello.py'
            }
        }
    }

    post {
        success {
            echo 'Build Successful!'
        }
        failure {
            echo 'Build Failed!'
        }
        always {
            echo 'Pipeline Finished!'
        }
    }
=======
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest test_loan.py'
            }
        }

    }

    post {

        success {
            echo 'Build Successful! Loan Eligibility Application Passed.'
        }

        failure {
            echo 'Build Failed! Please Fix the Errors.'
        }

        always {
            echo 'Pipeline Execution Completed.'
        }
    }
>>>>>>> 4c5735f2d44ff93aa67d8a97bc2d1303ab608383
}
