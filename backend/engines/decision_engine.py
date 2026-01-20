def decide_settings(phone: dict, target_type: str, lens: str) -> dict:
    """
    Decide camera settings based on phone capabilities, target type, and selected lens.
    """
    if not phone:
        return {
            "mode": "Auto",
            "iso": "Auto",
            "shutter": "Auto",
            "focus": "Auto",
            "tripod": False,
            "warning": "Phone specs not found"
        }

    settings = {
        "mode": "Pro",
        "iso": None,
        "shutter": None,
        "focus": "None",
        "tripod": False,
        "warning": None
    }

    main_cam = phone.get("main_camera", {})

    if target_type == "planet":
        settings["iso"] = "100-400"
        settings["shutter"] = "1/60 - 1/125"
        settings["focus"] = (
            "Manual → Infinity"
            if main_cam.get("manual_focus")
            else "Auto (tap on object)"
        )
        if lens == "telephoto":
            settings["tripod"] = True
        else:
            # FIXED: Typo fixed
            settings["warning"] = (
                "No optical zoom available. "
                "Planet will appear very small."
            )
        return settings

    if target_type == "deep_sky":
        settings["iso"] = "800-1600"
        settings["shutter"] = "10-20 sec"
        settings["tripod"] = True
        settings["focus"] = (
            "Manual → Infinity"
            if main_cam.get("manual_focus")
            else "Auto (lock focus)"
        )

        if not main_cam.get("pro_mode"):
            settings["warning"] = (
                "Pro mode not available. "
                "Results depend on automatic night mode."
            )

        return settings

    if target_type == "fast_object":
        settings["iso"] = "800–1600"
        settings["shutter"] = "5–10 sec"
        settings["tripod"] = True
        settings["focus"] = "Manual → Infinity"
        return settings

    settings["warning"] = "Target not recognized. Using safe defaults."
    settings["iso"] = "Auto"
    settings["shutter"] = "Auto"
    settings["focus"] = "Auto"

    return settings