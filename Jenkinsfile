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
                withEnv (["AWS_ACCESS_KEY_ID=$(env.AWS_ACCESS_KEY_ID)", "AWS_SECRET_ACCESS_KEY=$(env.AWS_SECRET_ACCESS_KEY)", "AWS_DEFAULT_REGION=$(env.AWS_DEFAULT_REGION)"]) {

                    sh 'docker login -u AWS -P $(ws ecr-public get-login-password --region eu-west-2) public.ecr.aws/g7i5x3t7'
                    sh 'docker build -t ecr-repoimg .'
                    sh ' docker tag ecr-repoimg:latest public.ecr.aws/g7i5x3t7/ecr-repoimg:"$BUILD_ID"'
                    sh 'docker push public.ecr.aws/g7i5x3t7/ecr-repoimg:"$BUILD_ID"'
                }



             


            }
        }
    }
}
