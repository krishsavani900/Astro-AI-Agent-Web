import os
from backend.ai.gemini import GeminiExplainer
from backend.ai.fallback import FallbackExplainer


def get_ai_explainer():
    if os.getenv("GEMINI_API_KEY"):
        return GeminiExplainer()
    return FallbackExplainer()