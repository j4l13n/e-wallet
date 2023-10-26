# Docker Installation Guide

This guide will walk you through the process of setting up a Docker environment for your project. Docker is a containerization platform that simplifies the process of deploying and running applications.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- Docker: You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

## Installation Steps

Follow these steps to set up and use Docker for your project:

### 1. Build Docker Containers

To build Docker containers for your project, run the following command in your project directory:

```bash
make build
```
This command uses Docker Compose to build the containers defined in your project's docker-compose.yml file.

### 2. Run Development Environment

To start your development environment, execute the following command:
```bash
make run-dev
```
This command stops and removes any existing containers and then brings up the environment defined in the docker-compose.yml file. It's designed for development purposes.

### 3. Run Database Migrations

If your project requires database migrations, you can run them with the following command:

```bash
make run-migrate
```
This command runs database migrations using the python manage.py migrate command within the application container.

### 4. Shell Access
You can access the shell of your application container for debugging or running commands using the following:

```bash
make shell
```
This will provide you with an interactive shell inside the container.

### 5. Running Tests
To run tests for your application, use the following command:

```bash
make test
```
This command executes tests within the application container using pytest or your specified testing framework.

### 6. Clean Up
To stop and remove all Docker containers for your project, run:

```bash
make clean
```
This is helpful for cleaning up your development environment.

### 7. Viewing Logs
To view the logs of your application container, you can use the following command:

```bash
make logs
```
This will display logs for the 'app' container, which can be useful for debugging.

### Conclusion
You now have Docker set up for Tekana-eWallet. You can use these commands to build, run, and manage your development environment efficiently. Docker simplifies the process of managing dependencies and ensures consistent environments across different systems.





