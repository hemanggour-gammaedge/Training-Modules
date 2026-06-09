import json
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import text, select
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate, UserResponse, UserUpdate
from app.dependencies import get_db
from app.redis_client import cache_client


app = FastAPI(
    title="FastAPI Learning Project",
    version="1.0.0",
)


@app.get(
    "/users",
    response_model=list[UserResponse],
)
def get_users(
    db: Session = Depends(get_db),
):
    users = db.scalars(
        select(User)
    ).all()

    return users


@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    cache_key = f"user:{user_id}"

    cached_user = cache_client.get(cache_key)

    if cached_user:
        return json.loads(cached_user)

    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    result = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }

    cache_client.setex(
        cache_key,
        60,
        json.dumps(result),
    )

    return result


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=201,
)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    user = User(
        username=payload.username,
        email=payload.email,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@app.patch(
    "/users/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
):
    user = db.get(
        User,
        user_id,
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    data = payload.model_dump(
        exclude_unset=True
    )

    for field, value in data.items():
        setattr(
            user,
            field,
            value,
        )

    db.commit()

    db.refresh(user)

    return user


@app.delete(
    "/users/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.get(
        User,
        user_id,
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    db.delete(user)

    db.commit()

    return {
        "message": "User deleted"
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
