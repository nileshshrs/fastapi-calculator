# app/main.py

import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from app import calculator

load_dotenv()  # Load .env variables


app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def root():
    return {"message": "Welcome to the Calculator API"}

@app.post("/add")
def add(op: Operation):
    return {"result": calculator.add(op.a, op.b)}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": calculator.subtract(op.a, op.b)}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": calculator.multiply(op.a, op.b)}

@app.post("/divide")
def divide(op: Operation):
    try:
        result = calculator.divide(op.a, op.b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run only if main
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
