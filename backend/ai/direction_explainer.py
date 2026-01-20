import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def explain_direction(target: str, direction_data: dict) -> str:
    prompt = f"""
You are a friendly astrophotography assistant.

Target: {target}

Direction details:
Look direction: {direction_data['look_direction']}
Altitude: {direction_data['altitude']}
Best time: {direction_data['best_time']}
Tip: {direction_data['tip']}

TASK:
Explain this to a normal user in simple, friendly language.
Do NOT change the direction or time.
Do NOT ask questions.
Keep it short (2–3 lines).
"""

    try:
        model = genai.GenerativeModel("gemini-3-flash-preview")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return ""