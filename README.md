# user-management-service

## Description
This project is a a simple user management and authentication system using [FastAPI](https://fastapi.tiangolo.com/) + [PostgreSQL](https://www.postgresql.org/).  

The current features include:
* User model
* Create, Read, Update, Delete web service endpoints
* Login endpoint
* Auto-generated API documentation

Multiple feature ideas are also listed in the [Further Improvements](docs/Further%20Improvements.md) document.

## Installation
The current state of the application is not meant for production use.
To install it for development or experimentation purposes, there are two approaches you can take:

1. [Developer Containers](https://code.visualstudio.com/docs/devcontainers/containers)
2. Manual configuration (not recommended)

## Usage
The recommended way to run the application is by using the following command:

```bash
uvicorn src.main:app --reload --host=0.0.0.0 --port=$FAST_API_PORT
```
