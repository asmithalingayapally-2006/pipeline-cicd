
pipeline {
    agent any

    stages {

        stage('Compile') {
            steps {
                bat '"C:\\Users\\linga\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m py_compile app.py test_app.py'
            }
        }

        stage('Testing') {
            steps {
                bat '"C:\\Users\\linga\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install pytest'
                bat '"C:\\Users\\linga\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pytest -v'
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
