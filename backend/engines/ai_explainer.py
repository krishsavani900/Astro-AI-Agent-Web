from backend.ai.gemini import GeminiExplainer
from backend.ai.fallback import FallbackExplainer
from backend.utils.prompt_loader import load_prompt

def get_explainer():
    """
    Returns the best available explainer.
    Uses Gemini if available, otherwise fallback.
    """
    try:
        return GeminiExplainer()
    except Exception:
        return FallbackExplainer()

def explain_decision(phone, target, lens, settings):
    summary = f"{lens.capitalize()} • ISO {settings['iso']} • {settings['shutter']} • Tripod"

    steps = [
        {
            "title": "Lens",
            "instruction": f"Use the {lens} lens to capture the {target.lower()} clearly."
        },
        {
            "title": "Exposure",
            "instruction": f"Set ISO to {settings['iso']} and shutter speed to {settings['shutter']}."
        },
        {
            "title": "Focus",
            "instruction": settings["focus"]
        },
        {
            "title": "Stability",
            "instruction": "Use a tripod to keep the phone steady."
        }
    ]

    return {
        "summary": summary,
        "steps": steps,
        "expectation": "You should get a clear image with visible surface details.",
        "confidence": "High"
    }

def explain_direction(target: str, direction_data: dict) -> str:
    try:
        explainer = get_explainer()
        template = load_prompt("direction_prompt.txt")

        prompt = template.format(
            target=target,
            look_direction=direction_data.get("look_direction", "Unknown"),
            altitude=direction_data.get("altitude", "Unknown"),
            best_time=direction_data.get("best_time", "Unknown"),
            tip=direction_data.get("tip", "")
        )

        # FIXED: calling the new standard method
        text = explainer.generate_content(prompt)
        return text.strip()

    except Exception as e:
        print(f"Error in explain_direction: {e}")
        return "Point your phone in the suggested direction during the recommended time for best clarity."
