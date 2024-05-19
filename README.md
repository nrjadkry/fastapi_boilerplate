# FastAPI Boilerplate with PostgreSQL and Docker

This is a boilerplate project for building web applications using FastAPI framework with PostgreSQL as the database backend, all orchestrated with Docker environment.

## Features

- **FastAPI**: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **PostgreSQL**: PostgreSQL is a powerful, open-source object-relational database system known for its reliability, robustness, and performance.
- **Pydantic**: Pydantic is used for data validation and settings management, enabling easy serialization and validation of data structures.
- **SQLAlchemy**: SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python, providing a full suite of well-known enterprise-level persistence patterns.
- **Alembic**: Alembic is a lightweight database migration tool for usage with SQLAlchemy, allowing for easy schema migrations.
- **Docker Compose**: Docker Compose is used for orchestrating the FastAPI application and PostgreSQL database within Docker containers.

## Prerequisites

Before getting started, ensure you have the following installed on your system:

- Docker
- Docker Compose

## Installation

1. Clone this repository:

    ```bash
    git clone git@github.com:nrjadkry/fastapi_boilerplate.git
    ```

2. Navigate into the project directory:

    ```bash
    cd fastapi-postgres-boilerplate
    ```

3. Create a `.env` file in the project root using the `env_sample.txt` provided.

   `cp env_sample.txt .env`

4. Create a docker-compose file. Update it according to your choice

   `cp docker-compose.local.yml docker-compose.yml`


5. Start the application and PostgreSQL database containers using Docker Compose:

    ```bash
    docker-compose up -d
    ```

## Usage

Once Docker containers are up and running, the FastAPI application will be available at `http://localhost:8001`.

## Project Structure

- **app**: Contains the main application code.
    - **api**: API routers and endpoints.
    - **core**: Core application modules and configurations.
    - **db**: Database related code including SQLAlchemy models and database connection setup.
    - **schemas**: Pydantic models for request/response payloads.
- **alembic**: Contains database migration scripts managed by Alembic.
- **tests**: Unit and integration tests.
- **docker-compose.yml**: Docker Compose configuration file for orchestrating the FastAPI application and PostgreSQL database.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.
