pipeline {
    agent any
    stages {
        stage('') {
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
    }
}