# Bot API (FastAPI) — Starter Pack

Un squelette **prêt pour Codex (Web)** : API FastAPI avec tests, lint et CI. Aucune dépendance réseau pendant les tests.

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

## Utiliser avec Codex (Web)

1. Pousse ce dépôt sur GitHub.
2. Dans ChatGPT, lance **Codex**, connecte GitHub et **créé un environment** sur ce repo.
3. Donne une tâche du style :
   > “Ajoute un endpoint `GET /invoices`, écris les tests, fais passer la CI, et ouvre une PR proprement décrite.”

Le sandbox Codex n’a pas d’Internet par défaut : ce pack et ses tests fonctionnent **offline**.

---

## Structure

```
app/
├─ main.py
├─ routers/
│  └─ bot.py
└─ schemas/
   └─ bot.py
tests/
.github/
 └─ workflows/ci.yml
AGENTS.md
requirements.txt
requirements-dev.txt
pyproject.toml
.env.sample
```

