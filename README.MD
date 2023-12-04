# Pushing and Pulling Docker Images from Amazon ECR
Welcome to this demo project where I'll guide you through setting up and using AWS CLI to manage Docker images on Amazon Elastic Container Registry (ECR). We'll be working with a two-tier Django app, with Django as the front end and a MySQL container as the backend.

Our journey begins by installing AWS CLI and configuring it with your access key. The focus of this demonstration is on creating an ECR repository and performing Docker image push and pull operations. To illustrate these processes, we'll start by running the Django app on your local machine. This involves configuring the MySQL server and Django app before creating a Docker image of it using a Dockerfile. Subsequently, we'll push this image into the ECR repository, showcasing the creation and utilization of repositories through AWS CLI.

Following the successful local execution of the Django app, we'll repeat the process for creating a Docker image and pushing it to ECR. The final steps involve pulling the Docker images from ECR and running them locally. As the demonstration concludes, we'll cover the cleanup process, including the deletion of repositories and images in AWS.


Installing aws cli
[Demo video](https://youtu.be/N4TAsmQwC_A)

Configuring aws cli
[Demo video](https://youtu.be/JCYmI2wT3DA)

Setting up mysql server for django app on the local host 
[Demo video](https://youtu.be/qJBYJE4j_xE)

Building docker image for mysql
[Demo video](https://youtu.be/-2wjklK1jGo)

Creating repository and pushing mysql image into ECR
[Demo video](https://youtu.be/FLvtWIImPpU)

Running Django app locally
[Demo video](https://youtu.be/EWpsgeivME0)

Building Docker image of django app
[Demo video](https://youtu.be/1BbKESCRnXQ)

Creating repository and pushing Django app image into ECR
[Demo video](https://youtu.be/a1hvKLWzANo)

Pulling images from ECR and running on local machine
[Demo video](https://youtu.be/vPS8RSykr6U)

Deleting images and repo from ECR
[Demo video](https://youtu.be/Tz6-OV53TLA)
