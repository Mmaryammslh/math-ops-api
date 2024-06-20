# Arithmetic Operations API

The repository contains a FastAPI application with two endpoints for performing arithmetic operations (multiplication and division) calling an external executable.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)

## Installation

Install the following requirements.

1. For the application:

```bash
pip install fastapi
```

2. To make an executable:

```bash
pip install pyinstaller
```

3. For sample unit tests:

```bash
pip install httpx
```

```bash
pip install pytest
```

## Usage

1. Convert Python script to Exe. file

```bash
pyinstaller --onefile operations.py

```
2. Run the FastAPI application:

```bash
uvicorn server:app --reload
```
3. Run the sample unit tests:

```bash
pytest test_server.py
```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

### Multiplication

- **Endpoint:** `/multiplication/{num1}/{num2}`
- **Method:** `GET`
- **Parameters:**
  - `num1` (integer): The first number.
  - `num2` (integer): The second number.
- **Response:**
  - `value1`: The first number.
  - `value2`: The second number.
  - `operation`: The performed operation (multiplication).
  - `result`: The result of the multiplication.
- **Errors:**
  - `400: Bad Request`, For too large numbers bigger than 100000.

### Division

- **Endpoint:** `/division/{num1}/{num2}`
- **Method:** `GET`
- **Parameters:**
  - `num1` (integer): The numerator.
  - `num2` (integer): The denominator.
- **Response:**
  - `value1`: The numerator.
  - `value2`: The denominator.
  - `operation`: The performed operation (division).
  - `result`: The result of the division.
- **Errors:**
  - `500: Internal Server Error`, Division by zero.

## Error Handling

- **404: Not Found,** Custom handler for not found errors.
  - Response: `{"message": "Not found. The requested resource does not exist."}`

- **422: Unprocessable Entity,** Custom handler for validation errors.
  - Response: `{"message": "Invalid numbers. The values must be an integer."}`
