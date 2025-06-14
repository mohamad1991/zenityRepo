# SUMMARY.md

## Overview

This project is a Dockerized Python web service that exposes two HTTP GET endpoints:

- `/secret`: Retrieves a secret from an AWS DynamoDB table.
- `/health`: Returns the application's health status.

The code is well-documented, designed for containerized deployment, and includes a continuous integration (CI) pipeline powered by **Travis CI** to automate builds and deployment to **Docker Hub**.

---

## Step-by-Step Development Process

### 1. Project Initialization

- Initialized a Python project using a minimal web framework (e.g., Flask).
- Added `boto3` to interact with AWS DynamoDB.
- Created a `Dockerfile` to containerize the application.
- Use `Travis` as a CI tool to build the Docker image and deploy it to `Dockerhub`
- Use `Pytest` to test the app, it is a minimal test suite
- Create docker-compose file for creating the container using `docker-compose up`
- Create bash script `verification.sh` to use it for getting the container build and run then test the two endpoints and finally kill it, I made some changes in the script because I did run it on mac, if you will going to runit on Linux please make the changes accordingly


---

### 2. Application Structure

├── app/

│   ├── __init__.py        
│   └── app.py             
├── tests/

│   └── test_app.py        
├── requirements.txt

├── Dockerfile

├── docker-compose.yml

---

### 3. Deploy to ECS in AWS

In the bonus step I decide to do the following:
Choosing ECS as the service to deploy the docker container to, is it the easiest way because it is Serverless – no need to manage EC2 instances and it is supports Docker out of the box
I have to say that in order to create such a thing first I need to create a Terraform project to manage the ECS ( it is a big project ) and also create the yaml file for the deployment, I attached the yaml file I have to say that I use the AI to create it ( I also did not test it )

