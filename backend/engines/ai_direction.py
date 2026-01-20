from backend.ai.gemini import GeminiExplainer


def get_ai_direction(target: str, location: str | None = None) -> dict:
    # It's better to use a factory or try/except here, but direct instantiation is okay for now
    try:
        client = GeminiExplainer()

        prompt = f"""
You are an astronomy assistant.

Target: {target}
Location: {location or "Unknown"}

Explain in simple terms:
1. Where in the sky to look (direction)
2. Approximate altitude
3. Best time to observe
4. One practical tip

Be clear, beginner-friendly, and realistic.
Avoid exact degrees if uncertain.
"""
        # FIXED: Method name updated
        text = client.generate_content(prompt)
    except Exception:
        text = "Could not retrieve AI direction data."

    return {
        "source": "ai_estimated",
        "explanation": text.strip()
    }
