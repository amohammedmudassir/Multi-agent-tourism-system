"""
Places tool using Overpass API to get tourist attractions.
"""
import requests
from typing import Dict, List, Optional
from .geocoding_tool import get_coordinates


def get_places_near_coordinates(latitude: float, longitude: float, limit: int = 5) -> Dict[str, any]:
    """
    Get tourist attractions near given coordinates using Overpass API.
    
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
        limit: Maximum number of places to return (default: 5)
        
    Returns:
        Dictionary with list of places and success status
    """
    try:
        # Overpass API query to find tourist attractions
        # Search within ~10km radius
        overpass_url = "https://overpass-api.de/api/interpreter"
        
        query = f"""
        [out:json][timeout:25];
        (
          node["tourism"~"^(attraction|museum|gallery|zoo|theme_park|monument|memorial|artwork)$"](around:10000,{latitude},{longitude});
          way["tourism"~"^(attraction|museum|gallery|zoo|theme_park|monument|memorial|artwork)$"](around:10000,{latitude},{longitude});
          relation["tourism"~"^(attraction|museum|gallery|zoo|theme_park|monument|memorial|artwork)$"](around:10000,{latitude},{longitude});
        );
        out body;
        >;
        out skel qt;
        """
        
        response = requests.post(overpass_url, data=query, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        places = []
        seen_names = set()
        
        if "elements" in data:
            for element in data["elements"]:
                if "tags" in element:
                    tags = element["tags"]
                    name = tags.get("name") or tags.get("tourism:name") or tags.get("alt_name")
                    
                    if name and name not in seen_names:
                        places.append(name)
                        seen_names.add(name)
                        
                        if len(places) >= limit:
                            break
        
        # If we didn't find enough places, try a broader search
        if len(places) < limit:
            query_broad = f"""
            [out:json][timeout:25];
            (
              node["tourism"](around:20000,{latitude},{longitude});
              way["tourism"](around:20000,{latitude},{longitude});
              relation["tourism"](around:20000,{latitude},{longitude});
            );
            out body;
            >;
            out skel qt;
            """
            
            try:
                response_broad = requests.post(overpass_url, data=query_broad, timeout=30)
                response_broad.raise_for_status()
                data_broad = response_broad.json()
                
                if "elements" in data_broad:
                    for element in data_broad["elements"]:
                        if "tags" in element:
                            tags = element["tags"]
                            name = tags.get("name") or tags.get("tourism:name") or tags.get("alt_name")
                            
                            if name and name not in seen_names:
                                places.append(name)
                                seen_names.add(name)
                                
                                if len(places) >= limit:
                                    break
            except:
                pass  # If broad search fails, use what we have
        
        if len(places) == 0:
            return {
                "success": False,
                "error": "No tourist places found",
                "places": []
            }
        
        return {
            "success": True,
            "places": places[:limit],
            "error": None
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"API error: {str(e)}",
            "places": []
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "places": []
        }


def get_places_for_location(place_name: str, limit: int = 5) -> str:
    """
    Get tourist places for a location by name.
    
    Args:
        place_name: Name of the place
        limit: Maximum number of places to return
        
    Returns:
        Formatted string with list of places or error message
    """
    # First get coordinates
    geo_result = get_coordinates(place_name)
    if not geo_result["success"]:
        return f"I don't know if {place_name} exists. Could not find coordinates for this place."
    
    # Then get places
    places_result = get_places_near_coordinates(
        geo_result["latitude"], 
        geo_result["longitude"], 
        limit
    )
    
    if not places_result["success"] or len(places_result["places"]) == 0:
        return f"Could not find tourist attractions for {place_name}."
    
    places = places_result["places"]
    places_list = "\n".join([f"- {place}" for place in places])
    
    return f"In {place_name} these are the places you can go:\n{places_list}"

