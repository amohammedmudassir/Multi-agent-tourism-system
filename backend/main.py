"""
FastAPI application entry point for the Tourism AI system.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from backend.api.routes import router
from fastapi.middleware.cors import CORSMiddleware


# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Tourism AI API",
    description="Multi-agent tourism system API",
    version="1.0.0"
)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can later restrict to your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api", tags=["tourism"])


@app.get("/")
async def root():
    """Root endpoint."""
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

