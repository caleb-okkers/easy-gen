from fastapi import FastAPI
from app.routers.ai import router as ai_router

app = FastAPI(
    title="EasyGen AI Backend",
    version="1.0"
)

# Register routes
app.include_router(ai_router, prefix="/ai", tags=["AI"])


@app.get("/")
def root():
    return {"message": "EasyGen AI Backend is running!"}
