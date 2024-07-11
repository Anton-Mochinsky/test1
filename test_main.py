import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_memes():
    response = client.get("/memes")
    assert response.status_code == 200

def test_create_mem():
    response = client.post("/memes",json={"text":"Test Meme","image_url":"example.com/image"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Test Meme"
    assert data["image_url"] == "example.com/image"

def test_update_mem():
    response = client.put("/memes/1",json={"text":"Updated Meme","image_url":"example.com/updated"})
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Updated Meme"
    assert data["image_url"] == "example.com/updated"

def test_delete_mem():
    response = client.delete("/memes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Mem deleted"
