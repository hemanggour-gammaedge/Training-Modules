# Frontend and Backend Responsibilities
Their are generally two main parts of the web application **Frontend** and **Backend** and they both have their own responsibilities

## Frontend
The user-facing part of the application
- Display UI
- Capture user input
- Validate basic form data
- Call backend APIs
- Handle client-side routing

## Backend
The server-side part of the application
- Business logic
- Authentication & authorization
- Database operations
- API creation
- Security enforcement
- Integration with external services

### How they work
- **Frontend:** When a user logs into website then the frontend takes the user credentials like `email` and `password` as input and then it send those credentials to the backend via *API*
- **Backend:** Then the backend checks the database for the user credential and approve if its an valid operation or not then it return the respective success/error response with JWT/session token

---

# Client Server Architecture
Most modern applications follow a **client server** model
```txt
Client -> Request -> Server
Client <- Response <- Server
```

## Client
A system requesting data from the *server*

**Example:**
- Browser
- Mobile/Desktop Application
- API Tool (Postman/Curl)

## Server
A system processing requests and returning responses to the *client*

**Example:**
- Uvicorn
- Gunicorn
- NGINX
- Django Application
- FastAPI Application

### How they work
```txt
Browser -> Backend Server -> Database -> Backend Server -> Browser
```

1. Clients initiate requests.
2. Servers process requests.
3. Multiple clients can connect to one server.
4. Servers often communicate with databases and other services.

---

# How the Web Works
When we type `google.com` many things happen behind the scenes

### Step 1: DNS Resolution
Human can't remember all the *IP addresses* of the websites so we give the IPs a name which is called *Domain name* but networking works on IP addresses so we have to map *domain name* with the site *IP address*

So to do the mapping we use **DNS (Domain Name Server)** and when we give it the domain name then it return its IP address that we can use to access the service

When we type `google.com` the browser checks the browser cache for that domain IP if its not found, then it checks system cache if still not found then it goes to ISP (Internet Service Provider) and if it still not found then it goes to the domain providers itself for the domain IP then it returns back to the browser/client

```txt
google.com -> 8.8.8.8
```

---

### Step 2: TCP Connection

Now that the browser has the IP address of the website, it needs to establish a connection with the server.

The internet communication is generally done using **TCP (Transmission Control Protocol)** which provides reliable communication between the client and server.

Before any data is sent, a process called **TCP Three-Way Handshake** happens.

```txt
Client -> SYN -> Server
Client <- SYN-ACK <- Server
Client -> ACK -> Server
```

1. Client sends a **SYN** request asking to establish a connection.
2. Server responds with **SYN-ACK** indicating it is ready.
3. Client sends **ACK** confirming the connection.

After this process both the client and server can communicate reliably.

---

### Step 3: HTTPS/TLS Handshake

Nowadays most websites use **HTTPS** instead of plain HTTP.

Before sending actual data, the browser and server perform a **TLS (Transport Layer Security) Handshake**.

The purpose of TLS is:

- Encrypt communication
- Verify server identity
- Prevent attackers from reading data

```txt
Browser <-> TLS Handshake <-> Server
```

After a successful handshake, all communication becomes encrypted.

---

### Step 4: HTTP Request

Once the connection is established, the browser sends an HTTP request to the server.

Example:

```http
GET /search?q=python HTTP/1.1
Host: google.com
User-Agent: Chrome
```

The request contains:

- HTTP Method (GET, POST, PUT, DELETE, etc.)
- URL/Path
- Headers
- Query Parameters
- Request Body (for POST/PUT/PATCH requests)

Example:

```txt
Browser -> HTTP Request -> Server
```

---

### Step 5: Server Processing

After receiving the request, the backend starts processing it.

The backend:

- Validate request data
- Authenticate the user
- Execute business logic
- Query the database
- Call external APIs
- Generate a response

Example:

```txt
Browser -> FastAPI -> PostgreSQL
```

If the user requests profile information:

1. Backend verifies JWT token.
2. Backend fetches user data from database.
3. Backend prepares the response.

---

### Step 6: HTTP Response

After processing, the server sends an HTTP response back to the client.

Example:

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "name": "John"
}
```

The response contains:

- Status Code
- Response Headers
- Response Body

Example:

```txt
Server -> HTTP Response -> Browser
```

---

### Complete Request Lifecycle

```txt
User enters google.com
        |
        v
DNS Resolution
        |
        v
Get Server IP
        |
        v
TCP Connection
        |
        v
TLS Handshake (HTTPS)
        |
        v
HTTP Request
        |
        v
Backend Processing
        |
        v
Database/API Calls
        |
        v
HTTP Response
        |
        v
Browser Renders Result
```

### Important Points

1. DNS converts domain names into IP addresses.
2. TCP establishes a reliable connection.
3. TLS encrypts communication.
4. HTTP is used to exchange requests and responses.
5. Backend processes the request and generates a response.
6. Browser renders the received response.

---

# HTTP Methods and Status Codes

HTTP methods define the action that should be performed on a resource.

## GET

Used to fetch data from the server.

```http
GET /users
```

Example:
- Get all users
- Get product details
- Get blog posts

---

## POST

Used to create new data.

```http
POST /users
```

Example:
- Register a user
- Create a blog post
- Create an order

---

## PUT

Used to completely replace existing data.

```http
PUT /users/1
```

Example:

Before:

```json
{
    "name": "John",
    "age": 20
}
```

Request:

```json
{
    "name": "John",
    "age": 25
}
```

The entire resource gets updated.

---

## PATCH

Used to partially update data.

```http
PATCH /users/1
```

Request:

```json
{
    "age": 25
}
```

Only specified fields are updated.

---

## DELETE

Used to remove a resource.

```http
DELETE /users/1
```

Example:
- Delete user
- Delete comment
- Delete order

---

# HTTP Status Codes

Status codes tell the client what happened with the request.

## 2xx - Success

Request completed successfully.

```http
200 OK
201 Created
204 No Content
```

### Examples

**200 OK**

```txt
User data fetched successfully
```

**201 Created**

```txt
New user created successfully
```

**204 No Content**

```txt
Resource deleted successfully
```

---

## 3xx - Redirection

The requested resource has moved.

```http
301 Moved Permanently
302 Found
```

Example:

```txt
http://example.com
        |
        v
https://example.com
```

---

## 4xx - Client Errors

The problem is on the client side.

```http
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
429 Too Many Requests
```

### Examples

**400 Bad Request**

Invalid request data.

**401 Unauthorized**

User is not authenticated.

**403 Forbidden**

User is authenticated but does not have permission.

**404 Not Found**

Requested resource does not exist.

**429 Too Many Requests**

Rate limit exceeded.

---

## 5xx - Server Errors

The problem is on the server side.

```http
500 Internal Server Error
502 Bad Gateway
503 Service Unavailable
```

### Examples

**500 Internal Server Error**

Unhandled exception in backend.

**502 Bad Gateway**

Reverse proxy received an invalid response.

**503 Service Unavailable**

Server is overloaded or under maintenance.

---

### Important Points

1. GET fetches data.
2. POST creates data.
3. PUT replaces data.
4. PATCH partially updates data.
5. DELETE removes data.
6. 2xx means success.
7. 4xx means client error.
8. 5xx means server error.
