def classify_target(target:str) -> str:
    target = target.lower().strip()
    planets = [
        "moon", "jupiter", "saturn", "mars", "venus", "mercury", "neptune", "uranus", "earth"
    ]
    deep_sky = [
        "andromeda", "orion nebula", "pleiades", "whirlpool galaxy", "eagle nebula", "sombrero galaxy", "milky way", "stars", "galaxy"
    ]
    fast_objects = [
        "meteor", "meteor shower", "satellite", "comet"
    ]
    if target in planets:
        return "planet"
    if target in deep_sky:
        return "deep_sky"
    if target in fast_objects:
        return "fast_object"
    return "unknown"