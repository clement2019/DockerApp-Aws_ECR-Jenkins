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

                   
                }



             


            }
        }
    }
}
