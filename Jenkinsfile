pipeline {
    agent any
    stages {
        stage('Checkout')
        {
            steps {

                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/arielokmi/Word-Of-Games.git']])
            }
        }
        stage('Bulid')
        {
            steps {
               bat 'docker build -t arielokmi/wordgames .'
            }
        }
        stage('Run')
        {
            steps {
                bat 'docker run -it -p 8777:8777 -d  arielokmi/wordgames'
            }
        }
    }
}
