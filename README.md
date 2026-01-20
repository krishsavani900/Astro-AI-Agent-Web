# 🔭 Astro AI Guide - Frontend Application

Your personal AI astrophotography assistant powered by Google Gemini AI.

## 📋 Overview

**Astro AI Guide** is a Streamlit-based web application that provides intelligent guidance for astrophotography. It analyzes your smartphone's camera capabilities and generates customized settings recommendations for photographing celestial objects like the Moon, planets, and stars.

### Key Features

- 📱 **Phone-Aware Recommendations**: Analyzes your specific smartphone model's camera specifications
- ✨ **Celestial Target Classification**: Intelligently classifies different types of astronomical objects
- 🎥 **Lens Selection Engine**: Recommends optimal lens settings based on target and phone capabilities
- ⚙️ **Smart Camera Settings**: Generates ISO, shutter speed, and other configuration recommendations
- 🧭 **Directional Guidance**: Provides step-by-step instructions on how to locate your target in the sky
- 🤖 **AI-Powered Explanations**: Uses Google Gemini AI to explain decisions and provide detailed instructions
- 🐛 **Debug Mode**: View raw data and AI responses for development purposes

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API Key (free at [Google AI Studio](https://aistudio.google.com/app/apikey))
- Required Python packages (see Installation)

### Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install required dependencies:**
   ```bash
   pip install streamlit google-generativeai
   ```

3. **Ensure backend modules are available** by checking the backend folder structure:
   ```
   backend/
   ├── engines/
   │   ├── phone_specs.py
   │   ├── target_classifier.py
   │   ├── lens_selector.py
   │   ├── decision_engine.py
   │   ├── ai_explainer.py
   │   ├── ai_direction.py
   │   └── direction_engine.py
   ```

### Running the Application

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

---

## 📖 How to Use

### 1. **Configure API Key**
   - In the left sidebar, enter your Google Gemini API Key
   - Get a free key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - This key is required to generate AI-powered recommendations

### 2. **Input Details**
   - **📱 Phone Model**: Enter your smartphone model (e.g., "Galaxy S23 Ultra", "iPhone 15 Pro")
   - **✨ Target**: Enter the celestial object you want to photograph (e.g., "Moon", "Jupiter", "Milky Way")

### 3. **Generate Guide**
   - Click the **🚀 Generate Guide** button
   - Wait for the AI to analyze your request

### 4. **View Results**
   The app displays:
   - **📸 Camera Setup**: Quick metrics for Lens, ISO, and Shutter Speed
   - **📝 Detailed Instructions**: Step-by-step guidance with tips
   - **🧭 Location Guide**: How to find your target in the night sky

### 5. **Debug Mode (Optional)**
   - Enable "Show Raw Debug Data" in the sidebar to view:
     - Raw API responses
     - Complete data structure
     - Phone specifications
     - Classification results

---

## 🏗️ Application Architecture

### Frontend Flow

```
User Input (Phone Model + Target)
         ↓
API Key Validation
         ↓
┌─────────────────────────────────────┐
│   ANALYSIS PIPELINE (8 Steps)       │
├─────────────────────────────────────┤
│ 1. Get AI Direction (Target info)   │
│ 2. Fetch Phone Specs                │
│ 3. Classify Target Type             │
│ 4. Select Lens Configuration        │
│ 5. Decide Camera Settings           │
│ 6. Generate Step Instructions       │
│ 7. Get Direction Data               │
│ 8. Generate Direction Explanation   │
└─────────────────────────────────────┘
         ↓
Display Results & Guidance
```

### Core Components

#### **User Interface**
- **Header Section**: Title and description
- **Sidebar**: API key input, debug mode toggle, developer credits
- **Input Form**: Two-column layout for phone model and target input
- **Results Display**: Metrics, expandable instructions, location guidance

#### **Backend Integration**
The app imports and orchestrates 7 backend engines:

1. **`phone_specs.py`** - Retrieves camera specifications for a given phone model
2. **`target_classifier.py`** - Classifies celestial objects (moon, planet, star, nebula, etc.)
3. **`lens_selector.py`** - Recommends lens settings based on phone and target
4. **`decision_engine.py`** - Calculates optimal camera settings (ISO, shutter speed, etc.)
5. **`ai_explainer.py`** - Generates human-readable explanations using Gemini AI
6. **`ai_direction.py`** - Provides directional guidance to locate targets
7. **`direction_engine.py`** - Retrieves static direction data for celestial objects

---

## 🎨 UI/UX Features

### Styling
- Custom red button styling (#ff4b4b) with white text
- Emoji-enhanced interface for intuitive navigation
- Responsive column layouts for different screen sizes
- Expandable sections for detailed information

### User Feedback
- Loading spinner during AI processing
- Error messages for missing inputs or API issues
- Warning messages for unrecognized phone models
- Success feedback through metrics display

---

## 🔧 Configuration & Environment

### Environment Variables
- `GEMINI_API_KEY`: Set by the app using user input

### Streamlit Configuration
- **Page Title**: "Astro AI Agent"
- **Page Icon**: 🔭
- **Layout**: Centered (optimized for desktop viewing)

---

## ⚠️ Error Handling

The application includes comprehensive error handling:

| Error Scenario | Response |
|---|---|
| No API Key provided | ❌ Error: "Please enter a Gemini API Key" |
| Missing Phone Model or Target | ❌ Error: "Please enter both fields" |
| Phone model not found | ⚠️ Warning: Uses generic defaults |
| API call failure | ❌ Error with exception details |
| Missing location data | ⚠️ Warning: "No location data available" |

---

## 🐛 Debug Mode

Enable "Show Raw Debug Data" in the sidebar to inspect:
- Complete API responses
- Phone specifications JSON
- Target classification results
- Lens configuration details
- Camera settings recommendations
- AI-generated explanations
- Direction data

This is useful for:
- Testing backend integrations
- Validating API responses
- Troubleshooting issues
- Understanding the decision pipeline

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | Latest | Web framework for UI |
| `google-generativeai` | Latest | Gemini AI API integration |
| `os` | Built-in | Environment variable management |

---

## 🤝 Integration with Backend

This frontend application expects the following backend structure:

```python
# Expected imports from backend
from backend.engines.phone_specs import get_phone_specs
from backend.engines.target_classifier import classify_target
from backend.engines.lens_selector import select_lens
from backend.engines.decision_engine import decide_settings
from backend.engines.ai_explainer import explain_decision, explain_direction
from backend.engines.ai_direction import get_ai_direction
from backend.engines.direction_engine import get_direction_data
```

Each engine should return data in the expected format (see Backend Documentation).

---

## 📝 Example Usage Scenario

### Scenario: Photographing the Moon with iPhone 15 Pro

1. **Input**:
   - Phone Model: `iPhone 15 Pro`
   - Target: `Moon`

2. **Processing**:
   - Fetches iPhone 15 Pro camera specs (48MP, f/1.78 aperture, etc.)
   - Classifies Moon as a bright, near-field celestial object
   - Selects appropriate lens (wide or telephoto)
   - Calculates ISO 100-200, fast shutter speed
   - Generates step-by-step instructions

3. **Output**:
   ```
   Camera Setup:
   - Lens: Wide Telephoto
   - ISO: 100
   - Shutter: 1/500s
   
   Instructions:
   - Set camera to night mode
   - Ensure ISO is between 100-200
   - Use a tripod for stability
   - Avoid zooming excessively
   
   Location:
   - The Moon is currently visible in the [Direction]
   - Look [Degrees] above the horizon
   - Best visibility: [Time range]
   ```

---

## 🔐 Security Notes

- ⚠️ **API Key**: Never hardcode or commit API keys to version control
- The app temporarily stores the API key in session memory only
- For production, consider using Streamlit secrets management
- All data is processed through official Google APIs

---

## 🐛 Troubleshooting

### Issue: "Phone model not found"
**Solution**: The backend database doesn't have that exact model. The app will use generic defaults. Try with a common model name.

### Issue: "An error occurred" with no details
**Solution**: 
1. Enable Debug Mode to see the full error
2. Check your Gemini API key is valid
3. Verify internet connection
4. Check backend engines are properly installed

### Issue: No explanation text appearing
**Solution**:
1. Verify Gemini API key is correct
2. Check API quota hasn't been exceeded
3. Ensure backend `ai_explainer.py` is working correctly

### Issue: "ModuleNotFoundError: No module named 'backend'"
**Solution**: Run the app from the correct directory or add the parent directory to Python path

---

## 🚀 Future Enhancements

- [ ] Support for manual camera settings input
- [ ] Historical data for celestial events
- [ ] Image upload and analysis
- [ ] Weather integration for optimal viewing conditions
- [ ] User preference saving
- [ ] Multi-language support
- [ ] Mobile app version

---

## 📄 License

© 2026 Krish Savani. All rights reserved.

---

## 👨‍💻 About the Developer

**Krish Savani**  
*AI/ML Engineer & Astrophotographer*

Created this application to make astrophotography accessible and intuitive for smartphone users.

---

## 🤝 Contributing

To improve this application:
1. Test with different phone models
2. Report bugs and feature requests
3. Suggest better celestial object classifications
4. Contribute backend engine improvements

---

## 📧 Support

For issues or questions:
- Check the troubleshooting section above
- Enable debug mode for detailed diagnostics
- Review backend engine logs
- Verify Gemini API credentials

---

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Astrophotography Tips](https://www.nasa.gov/content/what-you-can-see-in-the-night-sky/)
- [Phone Camera Specifications](https://www.gsmarena.com/)

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Status**: Active Development
