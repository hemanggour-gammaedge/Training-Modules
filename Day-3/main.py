import os
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from pwdlib import PasswordHash
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

# ==================================================
# CONFIG
# ==================================================

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

password_hash = PasswordHash.recommended()

security = HTTPBearer()

# ==================================================
# FAKE DATABASE
# ==================================================

users_db: dict[str, dict] = {}

# ==================================================
# SCHEMAS
# ==================================================

class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


# ==================================================
# PASSWORD HELPERS
# ==================================================

def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


# ==================================================
# JWT HELPERS
# ==================================================

def create_access_token(data: dict) -> str:
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload["exp"] = expire

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token expired",
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )


# ==================================================
# AUTH DEPENDENCY
# ==================================================

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    payload = decode_access_token(token)

    username = payload.get("sub")

    if not username:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload",
        )

    user = users_db.get(username)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user


# ==================================================
# REGISTER
# ==================================================

@app.post("/register")
def register(data: RegisterRequest):

    if data.username in users_db:
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    users_db[data.username] = {
        "username": data.username,
        "hashed_password": hash_password(data.password),
    }

    return {
        "message": "User registered successfully"
    }


# ==================================================
# LOGIN
# ==================================================

@app.post("/login")
def login(data: LoginRequest):

    user = users_db.get(data.username)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    if not verify_password(
        data.password,
        user["hashed_password"],
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    access_token = create_access_token(
        {
            "sub": user["username"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


# ==================================================
# PROTECTED ROUTE
# ==================================================

@app.get("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "username": current_user["username"]
    }
