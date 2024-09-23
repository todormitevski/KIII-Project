# CI/CD Project

This repository contains a project developed as part of a college course on CI/CD. The project utilizes Docker Compose, k3d, and Kubernetes manifests to deploy and manage the Django application.

## Running

1. Clone the repository.
2. Run the application:
   - Using docker:
     ```bash
     docker-compose up
     ```
   - Using kubernetes:
     ```bash
     k3d cluster create -s 1 -a 2 -p "8080:80@loadbalancer"
     ./apply_manifests
     ```
3. Access the app via your web browser after the deployment.

## Technologies Used

- Docker
- Kubernetes

## Todor Mitevski 213165
