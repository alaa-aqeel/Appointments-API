from fastapi.testclient import TestClient
from migrate import init_reset_database
from wsgi import app 


init_reset_database()

client = TestClient(app)



def test_error_login():

    resp = client.post("/api/login", json={
        "username": "test_username", 
        "password": "123456789"
    })
    
    assert resp.status_code == 422 
    data = resp.json()
    assert not data['detail']["ok"] # False 

def test_login():

    # create account 
    resp = client.post("/api/register", json={
        "username": "test_username_login", 
        "password": "123456789"
    })

    assert resp.status_code == 200 

    # login 
    resp = client.post("/api/login", json={
        "username": "test_username_login", 
        "password": "123456789"
    })
    
    assert resp.status_code == 200 
    data = resp.json()
    assert data['detail']["ok"]# True 
    assert data['detail']["data"].get("token", False) # True


    # get access token
    token = data['detail']["data"]["token"]

    # get info account 
    resp = client.get("/api/me", headers={
        "Authorization": f"Bearer {token}"
    })

    data = resp.json()
    assert resp.status_code == 200 
    assert data['username'] == 'test_username_login' # True 