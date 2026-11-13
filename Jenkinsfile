pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Compile') {
            steps {
                bat 'python -m py_compile app.py test_app.py'
            }
        }

        stage('Testing') {
            steps {
                bat 'python -m pip install pytest'
                bat 'python -m pytest -v'
            }
        }

        stage('Packaging') {
            steps {
                bat 'if not exist dist mkdir dist'
                bat 'powershell -Command "Compress-Archive -Path app.py,test_app.py -DestinationPath dist/python-app.zip -Force"'
                archiveArtifacts artifacts: 'dist/python-app.zip'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline Successful!'
        }

        failure {
            echo 'CI/CD Pipeline Failed!'
        }
    }
}