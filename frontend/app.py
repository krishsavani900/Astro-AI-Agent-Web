import streamlit as st
import os
import google.generativeai as genai

# IMPORT YOUR ENGINES DIRECTLY 🛠️
from backend.engines.phone_specs import get_phone_specs
from backend.engines.target_classifier import classify_target
from backend.engines.lens_selector import select_lens
from backend.engines.decision_engine import decide_settings
from backend.engines.ai_explainer import explain_decision, explain_direction
from backend.engines.ai_direction import get_ai_direction
from backend.engines.direction_engine import get_direction_data

# 🎨 Page Config
st.set_page_config(page_title="Astro AI Agent", page_icon="🔭", layout="centered")

# -----------------------------------------------------------------------------
# 💅 Custom CSS
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }
    /* Add a nice glow effect to the developer name */
    .dev-name {
        font-weight: bold;
        color: #ff4b4b;
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 🏠 Header & Sidebar
# -----------------------------------------------------------------------------
st.title("🔭 Astro AI Guide")
st.markdown("Your personal AI astrophotography assistant.")

with st.sidebar:
    st.header("⚙️ Configuration")

    # 🔑 USER API KEY INPUT
    user_api_key = st.text_input("🔑 Enter Gemini API Key", type="password")
    st.info("Get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey)")

    debug_mode = st.checkbox("Show Raw Debug Data", value=False)

    # ⭐ NEW SHOUTOUT SECTION ⭐
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer Credit")
    st.markdown("""
    Created with ❤️ by <span class='dev-name'>Krish Savani</span>

    *AI/ML Engineer & Astrophotographer(By Hobby)*
    """, unsafe_allow_html=True)

    # You can add your actual links here if you want!
    # st.link_button("GitHub Profile", "https://github.com/krishsavani900")
    # st.link_button("LinkedIn", "https://linkedin.com/in/your-profile")

# -----------------------------------------------------------------------------
# 📝 Input Form
# -----------------------------------------------------------------------------
with st.form("analysis_form"):
    col1, col2 = st.columns(2)
    with col1:
        phone_model = st.text_input("📱 Phone Model", placeholder="e.g. Galaxy S23 Ultra")
    with col2:
        target = st.text_input("✨ Target", placeholder="e.g. Moon, Jupiter")
    submitted = st.form_submit_button("🚀 Generate Guide")

# -----------------------------------------------------------------------------
# 🧠 Logic & Display
# -----------------------------------------------------------------------------
if submitted:
    if not user_api_key:
        st.error("❌ Please enter a Gemini API Key in the sidebar to proceed!")
        st.stop()

    # Configure the API Key globally for this session
    os.environ["GEMINI_API_KEY"] = user_api_key
    genai.configure(api_key=user_api_key)

    if not phone_model or not target:
        st.error("Please enter both a Phone Model and a Target!")
    else:
        with st.spinner("🤖 AI is analyzing celestial conditions..."):
            try:
                # --- DIRECT LOGIC PIPELINE ---

                # 1. Get AI Direction
                ai_direction = get_ai_direction(target)

                # 2. Get Phone Specs
                phone = get_phone_specs(phone_model.strip())
                if not phone:
                    st.warning(f"Phone '{phone_model}' not found. Using generic defaults.")

                # 3. Classify Target
                target_type = classify_target(target.strip())

                # 4. Select Lens
                lens = select_lens(phone, target_type)

                # 5. Decide Settings
                settings = decide_settings(phone, target_type, lens)

                # 6. Generate Explanation
                explanation = explain_decision(phone, target, lens, settings)

                # 7. Get Static Direction Data
                direction_data = get_direction_data(target)

                # 8. Generate Direction Explanation
                direction_explanation = explain_direction(target, direction_data)

                data = {
                    "lens": lens,
                    "settings": settings,
                    "explanation": explanation,
                    "direction_ai": ai_direction,
                    "direction": {
                        "data": direction_data,
                        "explanation": direction_explanation
                    }
                }

                # --- DISPLAY RESULTS ---
                st.divider()
                st.subheader("📸 Camera Setup")
                c1, c2, c3 = st.columns(3)
                c1.metric("Lens", data.get("lens", "Unknown").capitalize())
                c2.metric("ISO", data["settings"].get("iso", "Auto"))
                c3.metric("Shutter", data["settings"].get("shutter", "Auto"))

                with st.expander("📝 View Detailed Instructions", expanded=True):
                    explanation = data.get("explanation", {})
                    if isinstance(explanation, dict):
                        for step in explanation.get("steps", []):
                            st.markdown(f"**{step['title']}**: {step['instruction']}")
                        st.caption(f"💡 *Tip: {explanation.get('expectation', '')}*")
                    else:
                        st.write(explanation)

                st.subheader(f"🧭 How to Find {target}")
                if data["direction_ai"].get("explanation"):
                    st.markdown(data["direction_ai"]["explanation"])
                else:
                    st.warning("No location data available.")

                # Final Footer Shoutout
                st.divider()
                st.caption(f"© 2026 Krish Savani. All rights reserved.")

                if debug_mode:
                    st.divider()
                    st.json(data)

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")