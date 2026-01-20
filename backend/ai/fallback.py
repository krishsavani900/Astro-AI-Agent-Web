from backend.ai.base import AIExplainer

class FallbackExplainer(AIExplainer):
    def explain(self, phone, target, lens, settings) -> str:
        return (
            f"Lens: {lens}\n"
            f"ISO: {settings.get('iso', 'Auto')}\n"
            f"Shutter: {settings.get('shutter', 'Auto')}\n"
            f"Focus: {settings.get('focus', 'Auto')}\n"
            f"Tripod: {settings.get('tripod', False)}\n"
        )

    def generate_content(self, prompt: str) -> str:
        return "AI unavailable. Please check the standard guide."
