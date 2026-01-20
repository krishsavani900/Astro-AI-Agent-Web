from backend.engines.phone_specs import get_phone_specs
from backend.engines.target_classifier import classify_target
from backend.engines.lens_selector import select_lens
from backend.engines.decision_engine import decide_settings
from backend.engines.ai_explainer import explain_decision

phone = get_phone_specs("Galaxy S23 Ultra")
target = "Moon"

target_type = classify_target(target)
lens = select_lens(phone, target_type)
settings = decide_settings(phone, target_type, lens)

explanation = explain_decision(phone, target, lens, settings)

print("\n--- AI EXPLANATION ---\n")
print(explanation)