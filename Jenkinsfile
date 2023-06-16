pipeline{
    agent any
    environment {

        registry = "aws ecr get-login-password --region eu-west-2.759623136685.dkr.ecr.eu-west-2.amazonaws.com/ecr-repoimg1"
        dockerImage = ''
        }
      
      
        stages {

            stage('Create Docker image') {
                steps {
                    script {
                       dockerImage = docker build - t ecr-repoimg . + ":$BUILD_NUMBER"
                  }
              }
          }
          
          stage('Push Docker image to Docker Registry') {
            steps {
                script {
                    docker.withRegistry( "https://" + registry, "ecr:AWS_DEFAULT_REGION:AWS_ACCESS_KEY_ID") {
                    dockerImage.push()
                      }
                  }
              }
          }
          
      
        }
       
    }