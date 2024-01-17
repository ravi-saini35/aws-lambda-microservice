# aws-lambda-microservice

This project is all about the integration of different services on AWS, which includes Lambda, API Gateway, Amazon DynamoDB, DynamoDB streams, SNS, CloudWatch and IAM.



## Tech Stack

**Services:** Lambda, API Gateway, Amazon DynamoDB, DynamoDB streams, SNS, CloudWatch and IAM.

**Runtime env:** Python 3.9


## License



![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

## Roadmap and Architecture

The architecture goes here.

### 1. Lambda

Create a Lambda for CRUD operations on dynamoDB. Create a role to give access to dynamoDB, API gateway and cloudWatch to print logs.\
Use boto3 module to access different aws services.
sample code is in the file microservice_lambda.py  
  
Lambda code is given in the repository files.

### 2. API gateway
