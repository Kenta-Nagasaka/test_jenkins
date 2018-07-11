Jenkinsfile (Declarative Pipeline)

pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('build2') {
            steps {
                sh 'python --version'
            }
        }
    }
}
