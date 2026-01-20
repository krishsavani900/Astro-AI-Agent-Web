import os
import google.generativeai as genai
from backend.ai.base import AIExplainer
from backend.utils.prompt_loader import load_prompt

# Configure API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiExplainer(AIExplainer):
    def explain(self, phone, target, lens, settings) -> str:
        try:
            template = load_prompt("explainer_prompt.txt")

            prompt = template.format(
                phone_model=phone.get("model", "Unknown Phone"),
                target=target,
                lens=lens,
                iso=settings.get("iso", "Auto"),
                shutter=settings.get("shutter", "Auto"),
                focus=settings.get("focus", "Auto"),
                tripod=settings.get("tripod", "No"),
                warning=settings.get("warning", "")
            )

            model = genai.GenerativeModel("gemini-3-flash-preview")
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating explanation: {str(e)}"

    def generate_content(self, prompt: str) -> str:
        try:
            model = genai.GenerativeModel("gemini-3-flash-preview")
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating content: {str(e)}"
