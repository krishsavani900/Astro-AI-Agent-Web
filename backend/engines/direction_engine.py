def get_direction_data(target: str):
    target = target.lower().strip()

    if target == "moon":
        return {
            "look_direction": "East to South-East",
            "altitude": "30–60° above the horizon",
            "best_time": "30–90 minutes after moonrise",
            "tip": "Avoid shooting near the horizon to reduce atmospheric blur"
        }
    if target in ["jupiter", "saturn", "mars", "venus"]:
        return {
            "look_direction": "South",
            "altitude": "40–70° above the horizon",
            "best_time": "Late night to early morning",
            "tip": "Planets appear sharper when higher in the sky"
        }

    if target == "stars" or target == "milky way":
        return {
            "look_direction": "Away from city lights",
            "altitude": "Straight up (zenith)",
            "best_time": "Midnight with no moon",
            "tip": "Darker skies give better star visibility"
        }

    return {
        "look_direction": "Unknown",
        "altitude": "Unknown",
        "best_time": "Unknown",
        "tip": "No specific direction data available for this target."
    }
