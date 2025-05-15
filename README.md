# FastAPI Calculator API

A simple calculator API built with FastAPI demonstrating best practices by applying the [12-Factor App](https://12factor.net/) principles.

---

## What This Project Does

This API provides basic arithmetic operations — addition, subtraction, multiplication, and division — through HTTP POST endpoints.  
It showcases:

- Clean project structure
- Configuration via environment variables
- Concurrency with multiple workers
- Port binding via env variables
- Testing with `pytest`
- FastAPI automatic interactive docs (Swagger UI)

---

## Features

- Add, subtract, multiply, divide two numbers
- Proper error handling (e.g., division by zero)
- Environment-based configuration (`.env` file)
- Runs with `uvicorn` server and supports multiple workers
- Easily extensible for more complex operations

---

## Getting Started

### Prerequisites

- Python 3.10+
- Git
- `pip` for Python package management

---

### Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/fastapi-calculator.git
cd fastapi-calculator
