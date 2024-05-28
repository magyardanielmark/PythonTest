# Introduction to Docker build

## Story

You use a lot of Nginx and Flask based webpage solution and you're getting tired of having to set up things again and again, so based on your collegue's recomendation you decided to create a portable nginx-flask image.

## What are you going to learn?

- How to create a Dockerfile
- How to build, tag Docker image
- Uploading your images to an image repository

## Tasks

1. Put Nginx with Flask in a single Dockerfile and configure Nginx, so it can run Flask backend. Upload it to AWS ECR.
    - You have the Dockerfile.

2. Build your Docker image from your Dockerfile.
    - You have the built image.

3. Run your Docker image, and test if it is working on your environment.
    - Docker image is running.
    - Flask is running on localhost.

4. Tag, and upload your image in to AWS ECR.
    - You have credentials for AWS accounts.
    - You are logged in to the ECR with the usage of the Docker cli.

## General requirements

- You have Docker cli, Docker daemon installed on your computer, or Docker desktop if you are using macOS or Windows.

## Hints

- Tag your image with ECR URL before push
- If you made a failed docker image build, you will got an untagged image. In that case, you can only delete it with forced delete. Use ```docker rmi -f```.
- Use this command to login to ecr with docker ```aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ECR_URL>```
- The nginx and the flask application should be in one container, and you can start multiple services in one container in 2 ways, one is using supervisord to start the services, the other is using a custom start script which starts the other 2 services
- The docker container stops if the process is finishes

## Background materials

* <i class="far fa-book-open"></i> [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#from)
* <i class="far fa-book-open"></i> [Docker cli reference](https://docs.docker.com/engine/reference/commandline/cli/)
* <i class="far fa-book-open"></i> [Docker image build reference](https://docs.docker.com/engine/reference/commandline/image_build/)
* <i class="far fa-book-open"></i> [Docker image tag reference](https://docs.docker.com/engine/reference/commandline/image_tag/)
* <i class="far fa-book-open"></i> [Pushing a Docker image to ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)
* <i class="far fa-book-open"></i> [Start multiple services in one Docker container](https://docs.docker.com/config/containers/multi-service_container/)
