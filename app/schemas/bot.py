from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Message sent by the user."""

    message: str = Field(..., description="Message utilisateur")
    history: list[str] = Field(default_factory=list, description="Historique")


class ChatResponse(BaseModel):
    """Response returned by the bot."""

    reply: str
