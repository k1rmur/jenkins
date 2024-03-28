pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Convert the range to a list
                    def scriptNumbers = (1..3).toList()
                    for(x in scriptNumbers){
                        sh './test' + x + '.sh'
                    }
                }
            }
        }
    }
}