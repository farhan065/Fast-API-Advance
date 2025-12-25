from fastapi.testclient import TestClient
from app.main import app
from app import schemas

from tests.dbtest import client, session



### Testing root 
def test_root(client):
    response= client.get("/")
    assert response.status_code == 200
    assert response.json().get("Message") == "This is my first FastAPI application!!!!"


#### Testing user_create:
def test_user_create(client):
    response= client.post(
        "/users/",
        json={ "email": "gdf123@gmail.com", "password": "password123"}

    )
    new_user= schemas.UserResponse(**response.json())
    assert new_user.email == "gdf123@gmail.com"
    assert response.status_code == 201

#### Testing user login route
def test_user_login(client):
    response= client.post(
        "/login",
        data={ "username": "gdf123@gmail.com", "password": "password123"}### aikahne data use korsi jason er bodle karon form data hishebe input nisi latest version chaile json akare kora jabe but auth a giye login  er previous route uncomment kora lageb

    )
    assert response.status_code == 200
    
    

    
    
    

    