from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.dependencies import get_db

app = FastAPI(
    title="FastAPI Learning Project",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "API is running"
    }


@app.get("/health")
def health_check(
    db: Session = Depends(get_db)
):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
        }
