# CogoPort Assignment

## Introduction

This project implements a backend API using FastAPI for managing country configurations. It allows CRUD operations (Create, Read, Update, Delete) for country configurations, stored in a PostgreSQL database. The API includes endpoints to create new configurations, retrieve existing ones, update configurations, delete configurations, and fetch configurations by country code.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)
7. [Database Schema](#database-schema)


## Project Overview

### Description

The FastAPI project is designed to manage country configurations, providing RESTful endpoints to perform CRUD operations on a PostgreSQL database. It includes:
- **API Endpoints**: Create, read, update, delete country configurations.
- **Database Integration**: Uses SQLAlchemy ORM with Alembic for database migrations.
- **Validation**: Input validation using Pydantic models.
- **Documentation**: Automatically generated API documentation with Swagger UI.

### Key Features

- **CRUD Operations**: Create, Read, Update, Delete country configurations.
- **Validation**: Input validation with Pydantic models.
- **API Documentation**: Interactive API documentation with Swagger UI.
- **Database Migration**: Database schema management using Alembic.

## Technologies Used

- **FastAPI**: FastAPI framework for building APIs with Python 3.7+
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for database interaction
- **PostgreSQL**: Database management system
- **Alembic**: Database migration tool for SQLAlchemy
- **Pydantic**: Data validation and settings management using Python type hints
- **uvicorn**: ASGI server implementation for running FastAPI

## Installation

### Prerequisites

- Python 
- PostgreSQL

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/fastapi-project.git
    cd fastapi-project
    ```

2. **Set up virtual environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate #on windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Create a PostgreSQL database (e.g., `fastapi_db`).
    - Update the database connection URL in `alembic.ini` and `app/config.py`.

5. **Apply database migrations**:
    ```bash
    alembic upgrade head
    ```

6. **Run the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

### API Endpoints

- **Create Country Configuration**: `POST /countries/`
- **Get All Country Configurations**: `GET /countries/`
- **Get Country Configuration by ID**: `GET /countries/{id}`
- **Update Country Configuration**: `PUT /countries/{id}`
- **Delete Country Configuration**: `DELETE /countries/{id}`

## API Documentation

The API documentation can be accessed at `/docs` (e.g., http://localhost:8000/docs) which provides an interactive interface to test and explore the API endpoints.

## Database Schema

### Country Configuration

- **id**: Integer, primary key
- **country_code**: String(2), unique identifier for the country
- **business_name_required**: Boolean, whether business name is required
- **pan_number_required**: Boolean, whether PAN number is required
- **gstin_required**: Boolean, whether GSTIN is required



