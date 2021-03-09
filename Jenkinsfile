pipeline {
    agent any

    stages {        
        stage('Build'){
            steps{
                bat 'python main.py'
            }
        }
        stage('Test'){
            steps{
                echo 'the job has been tested'
            }
        }
        stage('Deploy'){
            steps{
                echo 'Deployed successfully'
            }
        }
    }
}
