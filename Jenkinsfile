pipeline {
<<<<<<< HEAD
    agent {
        docker {
            image 'python:3.9'  // Specify the Python version you need
        }
    }
=======
>>>>>>> 0666693 (python test)
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
    }
}
