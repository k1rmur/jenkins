pipeline {
    agent any
    stages {
        stage('Echo in files') {
            steps {
                script {
                    def scriptNumbers = (1..3).toList()
                    for(x in scriptNumbers){
                        sh 'sh_tests/test' + x + '.sh'
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
                sh 'python3 python_threading/doctor.py'
            }
        }
        stage('CPP Containers tests') {
            steps {
                sh 'cd CPP_containers'
                sh 'make'
            }
        }
        stage('CPP Containers clean') {
            steps {
                sh 'cd CPP_containers'
                sh 'make clean'
            }
        }
    }
}