from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from routes.admin import router

load_dotenv()

app = FastAPI(
    title="Gmail Alerter",
    version="1.0.0",
    description="A FastAPI application for Gmail alerts"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Gmail Alerter API",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = 8000
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=os.getenv("DEBUG", "True").lower() == "true"
    )
