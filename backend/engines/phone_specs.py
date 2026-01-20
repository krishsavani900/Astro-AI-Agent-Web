import json
import difflib
from pathlib import Path

# Load phones.json once (at import time)
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "phones.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    PHONES = json.load(f)

def get_phone_specs(phone_name: str) -> dict | None:
    """
    Retrieves phone specs with smart fuzzy matching.
    Example: "s24 ultra" -> returns "Galaxy S24 Ultra" specs.
    """
    # 1. Try Exact Match first (Fastest)
    if phone_name in PHONES:
        return PHONES[phone_name]

    # 2. Normalize input (lowercase, strip extra spaces)
    search_query = phone_name.lower().strip()
    
    # 3. Approach A: Substring Search
    # (Good for "s24 ultra" -> finding "Galaxy S24 Ultra")
    matches = []
    for key in PHONES.keys():
        if search_query in key.lower():
            matches.append(key)
    
    if matches:
        # If multiple matches found (e.g. "pixel 8" matches "Pixel 8" and "Pixel 8 Pro"),
        # pick the shortest one (usually the base model) to be safe.
        best_match = min(matches, key=len)
        return PHONES[best_match]

    # 4. Approach B: Typo Correction (Fuzzy Match)
    # (Good for "Glaxy S24" -> finding "Galaxy S24")
    # cutoff=0.5 means it needs to be 50% similar
    close_matches = difflib.get_close_matches(phone_name, PHONES.keys(), n=1, cutoff=0.5)
    
    if close_matches:
        return PHONES[close_matches[0]]

    # 5. If nothing found, return None 
    # (The system will then use the Default/Generic mode automatically)
    return None
