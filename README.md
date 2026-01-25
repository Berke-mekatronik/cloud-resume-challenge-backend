# Cloud Resume Challenge – Backend

This repository contains the backend implementation of my Cloud Resume Challenge project. The backend provides a serverless API that tracks and returns the number of visitors to the resume website. You can reach to the project from there: [Berke Ozturk Resume](https://s3.domain-of-berke.com/)

This project is based on the original challenge created by **Forrest Brazeal**: [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/)

## Architecture Diagram
![Architecture Diagram](/img/Architecture_Diagram.png)

## Infrastructure Components Created
The backend infrastructure is fully provisioned using **Terraform** and consists of:

* **AWS Lambda** for serverless compute
* **Amazon API Gateway** for HTTP API exposure
* **Amazon DynamoDB** for persistent visitor count storage
* **IAM** for secure access control
* Infrastructure fully managed using **Terraform**

## REST API Overview

- **Endpoint:** `GET /VisitorCounter`
- **Description:**  
  Retrieves the current visitor count from DynamoDB, increments it, and returns the updated value.

![API Method](/img/API_Method.png)

## Infrastructure as Code (Terraform)

All backend infrastructure is defined using Terraform, enabling:

- Reproducible deployments
- Easy teardown and recreation
- Safe infrastructure changes via `terraform plan`

### Terraform Workflow

```
terraform init
terraform plan
terraform apply
```

## CI/CD Deployment Flow
The backend is deployed automatically using GitHub Actions:

1. Code changes are pushed to the repository
2. Terraform initializes and validates the configuration
3. Infrastructure changes are applied automatically

AWS credentials are never committed to the repository and are securely managed via IAM roles / GitHub Actions secrets.

## Live Preview

![Preview_of_resume](/img/Preview_of_resume.png)

## Notes
This backend API is consumed by the frontend resume website to display a live visitor count.

Frontend Repository:
https://github.com/Berke-mekatronik/cloud-resume-frontend