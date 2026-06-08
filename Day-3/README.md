# FastAPI JWT Authentication

A simple FastAPI authentication example using:

* FastAPI
* JWT (PyJWT)
* Pwdlib for password hashing
* In-memory Python dictionary as a fake database

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Register User

```http
POST /register
```

Request Body:

```json
{
  "username": "hemang",
  "password": "secret123"
}
```

### Login User

```http
POST /login
```

Request Body:

```json
{
  "username": "hemang",
  "password": "secret123"
}
```

Response:

```json
{
  "access_token": "<jwt-token>",
  "token_type": "bearer"
}
```

### Get Current User

```http
GET /me
```

Header:

```http
Authorization: Bearer <jwt-token>
```

## Project Structure

```text
.
|-- main.py
|-- README.md
|-- .env.example
```
