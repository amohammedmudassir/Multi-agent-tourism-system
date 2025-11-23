"""
Tourism Agent - Parent orchestrator that combines weather and places information.
"""
from backend.agents.weather_agent import get_weather_info
from backend.agents.places_agent import get_places_info
from backend.tools.geocoding_tool import geocode_place


def get_tourism_info(place: str):
    """
    Get tourism information (weather and places) for a location.
    
    Args:
        place: Name of the place
        
    Returns:
        Dictionary with weather, places, and place_name
    """
    # Get place name from geocoding for display
    coords = geocode_place(place)
    place_name = coords.get("name") if coords else place
    
    weather = get_weather_info(place)
    places = get_places_info(place)

    return {
        "weather": weather,
        "places": places,
        "place_name": place_name
    }
