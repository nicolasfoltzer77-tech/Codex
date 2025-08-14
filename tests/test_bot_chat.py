from httpx import AsyncClient

from app.main import app


async def test_bot_greeting():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/bot/chat", json={"message": "Bonjour"})
        assert r.status_code == 200
        data = r.json()
        assert "Bonjour" in data["reply"] or "Salut" in data["reply"]


async def test_bot_echo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/bot/chat", json={"message": "foo"})
        assert r.status_code == 200
        assert r.json()["reply"] == "Tu as dit: foo"
