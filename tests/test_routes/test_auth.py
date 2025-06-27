def test_user_signup(client):
    #Add new user to DB
    response = client.post('/users/signUp', json={
        "name": "New User",
        "email": "new@example.com",
        "password": "newpass123"
    })

    #Assert
    assert response.status_code == 201
    assert "id" in response.json

def test_user_login(client):
    #Add the user to DB first
    client.post('/users/signUp', json={
        "name": "Login Test",
        "email": "login@example.com",
        "password": "loginpass"
    })
    
    #Login
    response = client.post('/users/login', json={
        "Email": "login@example.com",
        "Password": "loginpass"
    })

    #Assert
    assert response.status_code == 200
    assert "access_token" in response.json