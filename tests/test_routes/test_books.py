def test_create_book(client, auth_token):
    #add jwt to Authorization header
    headers = {"Authorization": f"Bearer {auth_token}"}

    #post book details 
    response = client.post('/books', json={
        "title": "Test Book",
        "price": 9.99,
        "release_date": "2023-01-01",
        "author_names": ["Test Author"],
        "category_names": ["Test Category"]
    }, headers=headers)

    #Assert
    assert response.status_code == 201
    assert response.json['title'] == "Test Book"

def test_get_books(client, auth_token):
    #add jwt to Authorization header
    headers = {"Authorization": f"Bearer {auth_token}"}

    #get all books
    response = client.get('/books', headers=headers)

    #Assert
    assert response.status_code == 200
    assert isinstance(response.json['books'], list)