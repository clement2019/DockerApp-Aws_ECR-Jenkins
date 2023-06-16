stage('Login ECR image') {
              
              steps {
                  
                  script {
                      sh "aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin A759623136685.dkr.ecr.eu-west-2.amazonaws.com"
                      sh "docker build -t ecr-repoimg1 ."
                      sh "docker push 759623136685.dkr.ecr.eu-west-2.amazonaws.com/ecr-repoimg1:latest"
                  }
              }
          }