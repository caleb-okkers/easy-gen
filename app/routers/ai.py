from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_service import generate_text

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate_ai_text(request: PromptRequest):
    result = generate_text(request.prompt)
    # Always return a dict with 'response'
    return {"response": result}
