pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out project from GitHub'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Student Registration project'
                echo 'HTML project build completed'
            }
        }

        stage('Test') {
            steps {
                bat 'python test.py'
            }
        }
    }

    post {
        success {
            echo 'Build and tests passed successfully!'
        }

        failure {
            echo 'Build or tests failed!'
        }
    }
}