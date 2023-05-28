pipeline {
    agent any
    environment {
      DOCKERHUB_CREDENTIALS = credentials('docker-hub')
    }
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

                bat 'docker run --name docker_run_test -p 8777:8080 -v Scores_volume:/app/Scores.txt  -i -t -d  arielokmi/wordgames'
            }
        }
        stage('Test'){
            steps{
                script{
                    bat 'docker exec  docker_run_test /bin/bash'
                    bat  'python ./Tests/e2e.py'
                }
            }
        }
        stage('Finalize'){
            steps{
                withDockerRegistry([ credentialsId: "docker-hub", url: "" ]) {
                    bat 'docker push arielokmi/wordgames:latest'
                }
                bat 'docker kill docker_run_test'
                }
            }
        }
    }