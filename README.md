# WebGuard

WebGuard is a web application built with Django for managing web security.

## Getting Started

To set up the project locally using VSCode, follow these steps:

1. Clone the repository:

   git clone https://github.com/hafiyuddin/WebGuard.git

2. cd webguard in VSCode Terminal

3. pip install -r requirements.txt

4. python manage.py migrate

5. python manage.py runserver

6. Access the web application in own browser at http://localhost:8000

# CI/CD Pipeline

This project includes a CI/CD pipeline using GitHub Actions for continuous integration and deployment. The pipeline consists of the following steps:

# 1. Build and Test
- Install dependencies
- Run functional tests using Django's built-in testing framework
- Run security scans using Bandit (We use '|| true' to ensure that the workflow continues even if the Bandit scan fails.)

# Workflow Configuration
The CI/CD workflow is defined in the .github/workflows/ci-cd.yml file. It is configured to trigger on pushes to the main or uat branch. Each step of the workflow is defined to ensure the proper functioning and security of the application.

# Security Scanning Tools

The following security scanning tools are integrated into the CI/CD pipeline:

Bandit: A security linter for Python code.
