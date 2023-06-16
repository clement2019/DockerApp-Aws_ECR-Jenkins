pipeline{
    agent any
    stages{
        stage('Build image'){
            steps{
                sh 'printenv'
               
               


            }
        
         }
        stage('push image to ECR'){
            steps{
                withEnv (["AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID}", "AWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY}", "AWS_DEFAULT_REGION=${env.AWS_DEFAULT_REGION}"]) {
                    sh "aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 759623136685.dkr.ecr.eu-west-2.amazonaws.com/ecr-repoimg1"
                    
                    sh 'docker build -t ecr-repoimg .'
                    sh 'docker tag ecr-repoimg1:latest 759623136685.dkr.ecr.eu-west-2.amazonaws.com/ecr-repoimg1:""$BUILD_ID""'
                    sh 'docker push 759623136685.dkr.ecr.eu-west-2.amazonaws.com/ecr-repoimg1:""$BUILD_ID""'

                   
                }



             


            }
        }
    }
}
