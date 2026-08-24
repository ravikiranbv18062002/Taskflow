from fastapi import FastAPI
from app.core.database import engine

app = FastAPI()


@app.get("/health")
def health_check():
    try:
        with engine.connect():
            return {
                "status": "ok",
                "database": "connected",
            }
    except Exception as e:
        print(f"Database connection error: {e}")
        return {
            "status": "error",
            "database": "disconnected",
        }

@app.get("/")
def root():
    return {"message": "Welcome to TaskFlow"}
