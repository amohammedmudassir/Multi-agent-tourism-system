"""
FastAPI application entry point for the Tourism AI system.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from backend.api.routes import router

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Tourism AI API",
    description="Multi-agent tourism system API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change later if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api", tags=["tourism"])


@app.get("/")
async def root():
    return {
        "message": "Tourism AI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/api/health",
            "query": "/api/query"
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
