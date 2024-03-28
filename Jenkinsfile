pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                for(x in 1..3){
                    sh './test' + x + '.sh'
                }
            }
        }
    }
}