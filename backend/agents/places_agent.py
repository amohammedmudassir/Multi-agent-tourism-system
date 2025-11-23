"""
Places Agent - Simple function-based tourist places provider.
"""
from backend.tools.geocoding_tool import geocode_place
from backend.tools.places_tool import get_places_near_coordinates


def get_places_info(place: str):
    """
    Get tourist places information for a location.
    
    Args:
        place: Name of the place
        
    Returns:
        Formatted places string or None if error
    """
    coords = geocode_place(place)
    if coords is None:
        return None

    result = get_places_near_coordinates(coords["lat"], coords["lon"])
    
    if not result.get("success") or not result.get("places"):
        return None
    
    # Format: "In {place} these are the places you can go:\n- {place1}\n- {place2}"
    places_list = result.get("places", [])
    places_str = "\n".join([f"- {p}" for p in places_list])
    
    return f"In {place} these are the places you can go:\n{places_str}"
