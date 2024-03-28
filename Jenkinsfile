pipeline {
    agent any
    stages {
        stage('Echo in files') {
            steps {
                script {
                    def scriptNumbers = (1..3).toList()
                    for(x in scriptNumbers){
                        sh './test' + x + '.sh'
                    }
                }
            }
        }
        stage('Python version check') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Python threading check output') {
            steps {
                sh 'python3 python_script/doctor.py'
            }
        }
        stage('CPP Containers tests') {
            steps {
                sh 'Make'
            }
        }
        stage('CPP Containers clean') {
            steps {
                sh 'Make clean'
            }
        }
    }
}