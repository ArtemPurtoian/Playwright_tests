# Automation testing with Python + Playwright

With this project, I aim to demonstrate my understanding of how to 
effectively automate UI interactions using Playwright.\
I have implemented:
- .env + env_reader.py to maintain environment configuration
- conftest.py with a fixture that starts a browser from the configuration
- Page Object Models with the classes representing the web pages, each having 
its methods
- test modules representing separate test suites, each having its test scripts
- Dockerfile, to run the scripts in a docker container
---
## 1. Prerequisites

Make sure you have Python installed on your machine.

* Clone the repository
  > git clone https://github.com/ArtemPurtoian/Playwright_tests.git

* Navigate to the project directory
  > cd Playwright_tests

* Install dependencies
  > pip install -r requirements.txt
---
## 2. Running the Tests on a local machine

  > pytest -vv

## 3. Running the Tests in a Docker container 

* Build an image
  > docker build -t playwright_tests .

* Run the container from the image
  > docker run playwright_tests

* Run bash within the container 
  > docker run -it playwright_tests bash
  
  > pytest -vv
---