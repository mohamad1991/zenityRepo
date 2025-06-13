# INSTRUCTIONS.md

## 📦 Project Setup Instructions

This guide will help you run and test the Python-based web service that interacts with AWS DynamoDB. The service is Dockerized and includes CI/CD integration with Travis CI and Docker Hub.

---

## 🔧 Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- (Optional) AWS CLI, if you want to test DynamoDB access manually
- Access to an AWS account with permissions to read from DynamoDB
- A DynamoDB table already created and populated with the expected schema

---



### Clone the Repository and run the bash script

```bash
git clone https://github.com/mohamad1991/zenityRepo.git
cd zenityRepo
./verification.sh
```
