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
                bat '''
                if not exist index.html (
                    echo ERROR: index.html does not exist
                    exit /b 1
                )

                findstr /i "<form" index.html >nul
                if errorlevel 1 (
                    echo ERROR: Form is missing
                    exit /b 1
                )

                findstr /i "type=" index.html >nul
                if errorlevel 1 (
                    echo ERROR: Form fields are missing
                    exit /b 1
                )

                findstr /i "<button" index.html >nul
                if errorlevel 1 (
                    echo ERROR: Submit button is missing
                    exit /b 1
                )

                echo All HTML tests passed!
                '''
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