# Trading Bot Scaffold

Un squelette **prêt pour Codex (Web)** pour expérimenter un bot de trading.
L'API FastAPI expose un simple bot de discussion et un simulateur d'ordres.
Une intégration Telegram basique permet d'envoyer des notifications.

> 🧠 Voir **[AGENTS.md](AGENTS.md)** pour les règles d’automatisation et la checklist PR.

## Lancer en local

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Ouvre http://127.0.0.1:8000/health et teste `/bot/chat` :
```bash
curl -X POST http://127.0.0.1:8000/bot/chat -H "Content-Type: application/json" -d '{"message":"Bonjour"}'
```

## Tests & Qualité

```bash
pytest -q
ruff check . && ruff format --check .
```

## Structure

```
app/
├─ main.py
├─ routers/
│  └─ bot.py
└─ schemas/
   └─ bot.py
services/
├─ simulator.py
└─ telegram.py
tests/
Dockerfile
docker-compose.yml
AGENTS.md
requirements.txt
requirements-dev.txt
pyproject.toml
.env.sample
```
