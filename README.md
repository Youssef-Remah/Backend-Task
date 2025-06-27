# Online Library System (Backend Task)

A web-based system for managing an online library, allowing users to sign up, log in, and manage books, authors, and categories.

## Tech Stack
- **Backend:** Python, Flask, SQLAlchemy
- **Database:** SQL Server
- **ORM:** SQLAlchemy
- **API Docs:** Swagger UI
- **Authentication:** JWT (Bearer Token)
- **Containerization:** Docker
- **Testing:** Pytest

## How to Run the System
> Make sure you have **Docker** and **Docker Compose** installed on your machine.
### 1. Clone the Repository
https://github.com/Youssef-Remah/Backend-Task.git

### 2. Build and Start the Containers
```
docker-compose up -d --build
```

## How to Test the API
Once the app is running:
### Access the Swagger UI
```
http://localhost:5000/apidocs
```

## Authorize with JWT
1. First, sign up via the `/signup` endpoint

2. Then log in via `/login` to get the JWT token

3. Click the **Authorize** button in Swagger and paste your token like this:
      ```
      Bearer YOUR_JWT_TOKEN_HERE
      ```

## Running Unit Tests
To run the unit tests using `pytest`, open a terminal inside the container and run:
```
docker-compose run web python -m pytest tests/
```
