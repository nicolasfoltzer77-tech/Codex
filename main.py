from fastapi import FastAPI
from app.routers import bot

app = FastAPI(title="Bot API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, bool]:
    return {"ok": True}


app.include_router(bot.router, prefix="/bot", tags=["bot"])
