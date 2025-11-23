"""
Weather tool using Open-Meteo API to get current weather and forecast.
"""
import requests
from typing import Dict, Optional


def get_weather_by_coordinates(latitude: float, longitude: float) -> Dict[str, any]:
    """
    Get current weather for given coordinates using Open-Meteo API.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        
    Returns:
        Dictionary with weather information including temperature and precipitation probability
    """
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,precipitation_probability",
            "timezone": "auto"
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if "current" not in data:
            return {
                "success": False,
                "error": "Weather data not available",
                "temperature": None,
                "precipitation_probability": None,
                "formatted": None
            }
        
        current = data["current"]
        temperature = current.get("temperature_2m", None)
        precipitation = current.get("precipitation_probability", None)
        
        if temperature is None:
            return {
                "success": False,
                "error": "Temperature data not available",
                "temperature": None,
                "precipitation_probability": None,
                "formatted": None
            }
        
        # Format the response
        if precipitation is not None:
            formatted = f"{int(temperature)}°C with a chance of {int(precipitation)}% to rain"
        else:
            formatted = f"{int(temperature)}°C"
        
        return {
            "success": True,
            "temperature": temperature,
            "precipitation_probability": precipitation,
            "formatted": formatted,
            "error": None
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"API error: {str(e)}",
            "temperature": None,
            "precipitation_probability": None,
            "formatted": None
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "temperature": None,
            "precipitation_probability": None,
            "formatted": None
        }


def get_weather_for_place(place_name: str) -> str:
    """
    Get weather for a place by name (geocodes first, then gets weather).
    
    Args:
        place_name: Name of the place
        
    Returns:
        Formatted weather string or error message
    """
    from .geocoding_tool import get_coordinates
    
    # First get coordinates
    geo_result = get_coordinates(place_name)
    if not geo_result["success"]:
        return f"I don't know if {place_name} exists. Could not find coordinates for this place."
    
    # Then get weather
    weather_result = get_weather_by_coordinates(geo_result["latitude"], geo_result["longitude"])
    if not weather_result["success"]:
        return f"Could not retrieve weather information for {place_name}."
    
    return f"In {place_name} it's currently {weather_result['formatted']}."

