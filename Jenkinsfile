pipeline{
    agent any
    stages{
        stage('Build image'){
            steps{
                sh 'printenv'
                sh 'docker build -t ecr-repoimg .'
               


            }
        
        }
    }
}