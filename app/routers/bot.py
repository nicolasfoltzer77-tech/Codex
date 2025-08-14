from fastapi import APIRouter

from app.schemas.bot import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Basic chat endpoint that echoes or greets."""
    if request.message.lower().startswith(("bonjour", "salut")):
        return ChatResponse(reply="Bonjour ! Que puis-je faire pour vous ?")
    return ChatResponse(reply=f"Tu as dit: {request.message}")
