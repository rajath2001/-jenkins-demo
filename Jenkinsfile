pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/rajath2001/-jenkins-demo.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 main.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}
