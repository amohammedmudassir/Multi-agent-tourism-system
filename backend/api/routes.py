"""
API routes for the tourism system.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from backend.agents.tourism_agent import get_tourism_info
from backend.utils.place_extractor import extract_place_name

router = APIRouter()


class Query(BaseModel):
    query: str


@router.post("/query")
def process_query(data: Query):
    """
    Process a tourism query and return weather and places information.
    
    Args:
        data: Query object with user query string
        
    Returns:
        Dictionary with weather and places information
    """
    # Extract place name from natural language query
    place = extract_place_name(data.query)
    
    # If extraction fails, use the query as-is
    if not place:
        place = data.query.strip()
    
    res = get_tourism_info(place)
    return res


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
