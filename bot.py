from pydantic import BaseModel, Field
from typing import List


class ChatRequest(BaseModel):
    message: str = Field(..., description="Message utilisateur")
    history: List[str] = Field(default_factory=list, description="Historique éventuel")


class ChatResponse(BaseModel):
    reply: str
