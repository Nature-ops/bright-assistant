from fastapi import APIRouter

from app.services.prompt_service import PromptService

router = APIRouter()

prompt_service = PromptService()


@router.get("/prompt")
def get_prompt():

    prompt = prompt_service.load("system_prompt.txt")

    return {
        "prompt": prompt
    }