from fastapi.testclient import TestClient
from migrate import init_reset_database
from wsgi import app 


init_reset_database()

client = TestClient(app)


def test_register():

    resp = client.post("/api/register", json={
        "username": "test_username", 
        "password": "123456789"
    })
    
    assert resp.status_code == 200 
    data = resp.json()
    assert data['detail']['ok'] # True 

def test_register_with_role():

    # create with role id 
    resp = client.post("/api/register",json={
            "username": "test_username010", 
            "password": "123456789",
            "role": 2
        }) 

    # exit()
    assert resp.status_code == 200 
    data = resp.json()
    assert data['detail']['ok'] # True
    assert data['detail']['data']['role']['id'] == 2

def test_create_with_unique_username():

    resp = client.post("/api/register",json={
            "username": "test_username010", 
            "password": "123456789",
        }) 

    assert resp.status_code == 403 
    data = resp.json()
    assert not data['detail']['ok'] # False  
    assert "unique" in data['detail']['errors'][0].lower() # False  

def test_error_missing_field_register():

    # create employee account 
    resp = client.post("/api/register",json={ 
            "username": "field_username"
        })   

    data = resp.json()
    
    assert resp.status_code == 422 
    assert not data['detail']['ok']
    assert "password" in data['detail']['errors'][0]['loc'] 

def test_create_with_notfound_role():

    resp = client.post("/api/register",json={
            "username": "test_username0101", 
            "password": "123456789",
            "role": 21
        }) 

    assert resp.status_code == 422 
    data = resp.json()
    assert not data['detail']['ok'] # False 
    assert 'role' in  data['detail']['errors'][0]['loc'] # False 