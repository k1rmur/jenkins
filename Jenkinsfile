pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    for(x in 1..3){
                        sh 'chmod +x ./test' + x + '.sh'
                        sh './test' + x + '.sh'
                    }
                }
            }
        }
    }
}