"""
Utility to extract place names from natural language user input.
"""
import re
from typing import Optional, List


def extract_place_name(user_input: str) -> Optional[str]:
    """
    Extract place name from user input using pattern matching.
    
    Common patterns:
    - "I'm going to go to [PLACE]"
    - "I'm going to [PLACE]"
    - "Let's go to [PLACE]"
    - "What about [PLACE]"
    - "[PLACE] weather"
    - "[PLACE] places"
    
    Args:
        user_input: Natural language input from user
        
    Returns:
        Extracted place name or None if not found
    """
    if not user_input:
        return None
    
    # Common patterns to extract place names
    patterns = [
        r"(?:going to|go to|visit|travel to|heading to|planning to visit)\s+(?:the\s+)?([A-Z][a-zA-Z\s,]+?)(?:\s|,|\.|$|let|what|and|or)",
        r"([A-Z][a-zA-Z\s]+?)\s+(?:weather|temperature|climate)",
        r"([A-Z][a-zA-Z\s]+?)\s+(?:places|attractions|tourist|sights)",
        r"in\s+([A-Z][a-zA-Z\s]+?)(?:\s|,|\.|$|it|the|these)",
        r"at\s+([A-Z][a-zA-Z\s]+?)(?:\s|,|\.|$|it|the|these)",
    ]
    
    # Try each pattern
    for pattern in patterns:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            place = match.group(1).strip()
            # Clean up common words
            place = re.sub(r'\b(the|a|an|to|in|at|for|with)\b', '', place, flags=re.IGNORECASE).strip()
            if place and len(place) > 2:
                return place
    
    # If no pattern matches, try to find capitalized words (likely place names)
    # Look for sequences of capitalized words
    capitalized_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b'
    matches = re.findall(capitalized_pattern, user_input)
    
    if matches:
        # Filter out common words that aren't places
        common_words = {'I', 'I\'m', 'Let', 'Let\'s', 'What', 'Where', 'When', 'How', 
                       'The', 'This', 'That', 'These', 'Those', 'And', 'Or', 'But'}
        
        for match in matches:
            if match not in common_words and len(match) > 2:
                # Check if it's followed by place-related keywords OR if it's a simple query (just the place name)
                context = user_input.lower()
                is_simple_query = len(user_input.strip().split()) <= 3  # Simple queries like "Paris" or "New York"
                has_place_keywords = any(keyword in context for keyword in ['weather', 'temperature', 'places', 'attractions', 'visit', 'go', 'travel'])
                
                if has_place_keywords or is_simple_query:
                    return match
    
    # If still no match and input is short, assume it's a place name
    if len(user_input.strip().split()) <= 2:
        return user_input.strip()
    
    return None


def extract_place_simple(user_input: str) -> str:
    """
    Simple extraction that returns the input if no place is found.
    Useful as fallback.
    
    Args:
        user_input: User input string
        
    Returns:
        Extracted place name or original input
    """
    place = extract_place_name(user_input)
    if place:
        return place
    
    # Fallback: return the input as-is (let the geocoding API handle it)
    return user_input.strip()

