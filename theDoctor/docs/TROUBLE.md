# TROUBLE.md

## Troubleshooting and Challenges Faced

### 1. Wrong scheme DynamoDB

**Issue:**  
First when I try to run the GET request to get the secret I faced an issue in the scheme I tried to fix it buy add more fields or by making sure that I am doing the right thing.

**Solution:**  
After a while I realized that the issue is in the scheme not from my side I send email and get the scheme correction it is not `secret_code` but `secretCode`
---

### 2. Handling AWS Credentials Securely in Docker

**Issue:**  
Managing AWS credentials inside Docker containers posed a risk of exposing secrets or hardcoding sensitive info.

**Solution:**
- Used environment variables for AWS credentials and DynamoDB table name, passed at container runtime.

---

### 3. Network in the Docker container

**Issue:**  
The GET requests works locally but failed in the Docker container.

**Solution:**
I realized that the localhost inside the Docker container is not the same localhost locally, for fix this issue I change the server from 127.0.0.1 to 0.0.0.0
---

### 4. Docker Image Size and Build Time

**Issue:**  
Initial Docker images were large and slow to build.

**Solution:**
- Switched to a minimal base image (`python:3.11-slim`) to reduce image size.
- Used `pip install --no-cache-dir` to avoid caching during install.
- Added `.dockerignore` to exclude unnecessary files from the build context.

---

### 5. Automating CI/CD with Travis CI

**Issue:**  
Setting up Travis CI to build and push Docker images was initially tricky, especially handling Docker Hub authentication securely.

**Solution:**
- Stored Docker Hub credentials as encrypted environment variables in Travis.
- Used the recommended `docker login` with password piped from environment variables.
- Added clear scripts in `.travis.yml` to build and push images on each commit.

---

### 6. Pytest works locally but not in Travis

**Issue:**  
In Travis build I face issue iin running the tests, the error was that there is no app module

**Solution:**
I realized that I need to configure Python path `export PYTHONPATH=.` this fix the issue
