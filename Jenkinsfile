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
               bat 'docker build -t docker_build .'
            }
        }
        stage('Run')
        {
            steps {

                bat 'docker run --name docker_run -p 8777:8080  -i -t -d  docker_build'
            }
        }
        stage('Test'){
            steps{
                script{
                    bat 'docker exec  docker_run /bin/bash'
                    bat  'python ./Tests/e2e.py'
                }
            }
        }
    }
    post {
        always {
            bat 'docker kill docker_run'
        }
    }
}