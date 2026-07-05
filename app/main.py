from fastapi import FastAPI

app = FastAPI(
    title="Bright Assistant",
    description="AI-powered Engineering Assistant",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Bright Assistant!",
        "version": "0.1.0",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
