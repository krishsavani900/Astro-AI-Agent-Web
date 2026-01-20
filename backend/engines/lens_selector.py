def select_lens(phone: dict, target_type: str) -> str:
    if not phone:
        return "main"

    if target_type == "planet":
        tele = phone.get("telephoto_camera", {})
        available = tele.get("available", False)

        # FORCE boolean check
        if isinstance(available, str):
            available = available.lower() == "true"

        if available:
            return "telephoto"

        return "main"

    if target_type == "deep_sky":
        ultra = phone.get("ultrawide_camera", {})
        if ultra.get("pro_mode") and ultra.get("manual_focus"):
            return "ultrawide"
        return "main"

    if target_type == "fast_object":
        ultra = phone.get("ultrawide_camera", {})
        if ultra:
            return "ultrawide"
        return "main"

    return "main"