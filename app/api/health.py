from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Welcome to Bright Assistant!",
        "version": "0.1.0",
        "status": "Running"
    }

@router.get("/health")
def health():
    return{
        "status": "healthy"
    }
