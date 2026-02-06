from fastapi import APIRouter
from pydantic import BaseModel

from app.core.intentClassifier import detect_intent
from app.core.vectorStore import search_similar
from app.services.actionRouter import route_action
from app.services.chatService import return_message

router = APIRouter()


# BaseModel = Python’s version of a DTO + Validator + JSON mapper
class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(req: ChatRequest):
    return return_message(req.message)

