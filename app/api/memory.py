from fastapi import APIRouter

from app.services.memory_service import MemoryService

router = APIRouter()

memory = MemoryService()


@router.get("/memory")
def get_memory():

    return memory.history()


@router.get("/memory/stats")
def memory_stats():

    return memory.stats()


@router.delete("/memory")
def clear_memory():

    memory.clear()

    return {
        "message": "Conversation memory cleared."
    }