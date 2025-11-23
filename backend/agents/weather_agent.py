"""
Weather Agent - Simple function-based weather information provider.
"""
from backend.tools.weather_tool import get_weather_by_coordinates
from backend.tools.geocoding_tool import geocode_place


def get_weather_info(place: str):
    """
    Get weather information for a place.
    
    Args:
        place: Name of the place
        
    Returns:
        Formatted weather string or None if error
    """
    coords = geocode_place(place)
    if coords is None:
        return None
    
    result = get_weather_by_coordinates(coords["lat"], coords["lon"])
    
    if not result.get("success"):
        return None
    
    # Format: "In {place} it's currently {formatted}"
    formatted = result.get("formatted", "")
    if formatted:
        return f"In {place} it's currently {formatted}."
    
    return None
