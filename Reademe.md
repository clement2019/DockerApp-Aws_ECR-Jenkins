## Project title: Dokcerapp-AWs-ECR-Jenkins
#project Summary: 
This project demonstrates the process of dockerising a python fllask application, the Dockerfile was created wile there is a requirements.txt file housing all the dependencies.The docker image build is done using jenkins tool while the build image is stored inside Aws Elastic container registry (ECR).
This dockerised image can be used for deployment into kubernetes cluster either minikube or aws eks at anytime, this will be done in subsequesnt project, however let me reterate that this project is only concerned with python flask dockerisation and the the integration of AWs and jenkins automation for now i shall be dealling with deployment into kubernetes in latter project.
## Requirements and tools used
python Flask
Aws services
Jenkins
Docker

##  perequisiste and project installations
Install flask

Install python

Have an AWs account free tier
Create IAM user with secreste key and access key to be able to allow jenkins to be able to connect into aws infrastructure

Install  and configure jenkins on ubuntu 22.04 server (Ec2 instance) using managment console or using terraform to provision and install jebkins installation scripts

Open port 22 for ssh connections into the  jenkins instance
open port 8080 to be able to connect to jenkins dashboard

## project workflow




