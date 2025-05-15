# FastAPI Calculator API

A simple calculator API built with FastAPI demonstrating the application of the [12-Factor App](https://12factor.net/) principles.

---

## What This Project Does

This API provides basic arithmetic operations (addition, subtraction, multiplication, division) accessible via HTTP POST requests.  
It is designed with clean architecture, environment-based configuration, proper error handling, and automated testing to demonstrate best practices for scalable, maintainable API services.

---

## Features

- Addition, subtraction, multiplication, and division endpoints  
- Proper error handling (e.g., division by zero returns a 400 error)  
- Configuration via `.env` environment variables using `python-dotenv`  
- Runs with `uvicorn` ASGI server with hot reload for development  
- Interactive OpenAPI/Swagger documentation available at `/docs`  
- Automated testing with `pytest`  
- Easily extensible for more complex operations  
- Supports concurrency and multiple workers (production ready)  

---

## Getting Started

### Prerequisites

- Python 3.10 or higher  
- Git  
- `pip` package manager  

---

### Installation on Windows

1. Clone the repository:

    ```powershell
    git clone https://github.com/nileshshrs/fastapi-calculator.git
    cd fastapi-calculator
    ```

2. Create and activate a virtual environment:

    ```powershell
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install dependencies:

    ```powershell
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root (optional, default port is 8000):

    ```
    PORT=8000
    ```

---

### Running the Application

Run the FastAPI server with:

```powershell
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
