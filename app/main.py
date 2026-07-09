from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.api.prompt import router as prompt_router
from app.api.memory import router as memory_router

from app.config.settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered Engineering Assistant",
    version=settings.VERSION,
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(prompt_router)
app.include_router(memory_router)