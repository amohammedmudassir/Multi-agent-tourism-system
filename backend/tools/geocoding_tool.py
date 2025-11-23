"""
Geocoding tool using Nominatim API to get coordinates from place names.
"""
import requests
from typing import Dict, Optional


def get_coordinates(place_name: str) -> Dict[str, any]:
    """
    Get coordinates (latitude, longitude) for a place using Nominatim API.
    
    Args:
        place_name: Name of the place to geocode
        
    Returns:
        Dictionary with 'latitude', 'longitude', 'name', and 'success' keys
    """
    try:
        # Call Nominatim API
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": place_name,
            "format": "json",
            "limit": 1
        }
        headers = {
            "User-Agent": "Tourism-AI-Agent/1.0"
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if not data or len(data) == 0:
            return {
                "success": False,
                "error": "Place not found",
                "latitude": None,
                "longitude": None,
                "name": None
            }
        
        result = data[0]
        return {
            "success": True,
            "latitude": float(result.get("lat", 0)),
            "longitude": float(result.get("lon", 0)),
            "name": result.get("display_name", place_name),
            "error": None
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"API error: {str(e)}",
            "latitude": None,
            "longitude": None,
            "name": None
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "latitude": None,
            "longitude": None,
            "name": None
        }


def geocode_place(place_name: str) -> Optional[Dict[str, any]]:
    """
    Geocode a place and return coordinates as a dictionary.
    
    Args:
        place_name: Name of the place
        
    Returns:
        Dictionary with 'lat' and 'lon' keys, or None on error
    """
    result = get_coordinates(place_name)
    if result["success"]:
        return {
            "lat": result["latitude"],
            "lon": result["longitude"],
            "name": result["name"]
        }
    return None

