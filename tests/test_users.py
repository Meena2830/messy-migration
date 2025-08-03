# test_user.py

import pytest
from httpx import AsyncClient
from app.main import app  # Adjust import path if your app is elsewhere

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running"}

@pytest.mark.asyncio
async def test_create_user():
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json=user_data)
    assert response.status_code == 201
    assert "id" in response.json()

@pytest.mark.asyncio
async def test_get_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_login():
    credentials = {
        "email": "john@example.com",
        "password": "password123"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/login", json=credentials)
    assert response.status_code == 200
    assert "message" in response.json()
