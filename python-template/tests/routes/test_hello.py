def test_hello(client):
    # Act
    response = client.get("/hello-world")

    # Assert
    assert response.status_code == 200
