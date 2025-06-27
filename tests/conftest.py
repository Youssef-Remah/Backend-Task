import pytest
from app import create_app
from app.models import db as _db

@pytest.fixture
def app():
    #Create a new Flask application and with in-memory SQLite database
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

@pytest.fixture
def client(app):
    #Simulates the HTTP requests
    return app.test_client()

@pytest.fixture
def auth_token(client):

    #Create a test user and return JWT token
    test_user = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "testpass123"
    }

    client.post('/users/signUp', json=test_user)
    res = client.post('/users/login', json={
        "Email": "test@example.com",
        "Password": "testpass123"
    })

    return res.json['access_token']