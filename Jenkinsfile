pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    for(x in 1..3){
                        sh './test' + x + '.sh'
                    }
                }
            }
        }
    }
}