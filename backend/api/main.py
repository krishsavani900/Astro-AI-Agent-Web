from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import engines
from backend.engines.phone_specs import get_phone_specs
from backend.engines.target_classifier import classify_target
from backend.engines.lens_selector import select_lens
from backend.engines.decision_engine import decide_settings
from backend.engines.ai_explainer import explain_decision, explain_direction
from backend.engines.ai_direction import get_ai_direction
from backend.engines.direction_engine import get_direction_data

app = FastAPI()

# ------------------------------------------------------------------
# 🔓 CORS Configuration (Required for Deployment)
# ------------------------------------------------------------------
# This allows your Frontend (Streamlit) to talk to this Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change to specific URL in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# ------------------------------------------------------------------
# 🏠 Root Endpoint
# ------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "AI Agent is running 🚀"}


# ------------------------------------------------------------------
# 📨 Data Model
# ------------------------------------------------------------------
class AnalyzeRequest(BaseModel):
    phone_name: str
    target: str


# ------------------------------------------------------------------
# 🔭 Analyze Endpoint
# ------------------------------------------------------------------
@app.post("/analyze")
def analyze(data: AnalyzeRequest):
    # 1. Get AI Direction (pure AI)
    ai_direction = get_ai_direction(data.target)

    # 2. Get Phone Specs
    try:
        phone = get_phone_specs(data.phone_name.strip())
    except ValueError as e:
        return {"error": str(e)}

    # 3. Classify Target
    target_type = classify_target(data.target.strip())

    # 4. Select Lens
    lens = select_lens(phone, target_type)

    # 5. Decide Settings
    settings = decide_settings(phone, target_type, lens)

    # 6. Generate Explanation (Hybrid AI/Logic)
    explanation = explain_decision(phone, data.target, lens, settings)

    # 7. Get Static Direction Data
    direction_data = get_direction_data(data.target)

    # 8. Generate Direction Explanation (AI)
    direction_explanation = explain_direction(data.target, direction_data)

    return {
        "phone": data.phone_name,
        "target": data.target,
        "lens": lens,
        "settings": settings,
        "direction_ai": ai_direction,
        "direction": {
            "data": direction_data,
            "explanation": direction_explanation
        },
        "explanation": explanation
    }
