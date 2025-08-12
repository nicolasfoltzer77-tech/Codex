import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_bot_greeting():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/bot/chat", json={"message": "Bonjour"})
        assert r.status_code == 200
        data = r.json()
        assert "Salut" in data["reply"] or "Bonjour" in data["reply"]


@pytest.mark.asyncio
async def test_bot_echo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/bot/chat", json={"message": "foo"})
        assert r.status_code == 200
        assert r.json()["reply"] == "Tu as dit: foo"
