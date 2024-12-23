# Audience Navigator 🚀

## Overview
The **Audience Navigator** is a Streamlit-based application powered by **Lyzr Automata SDK**. It helps businesses develop tailored marketing strategies and actionable steps by analyzing their company information, goals, and target audience. The app leverages advanced AI models to provide insights into audience demographics, interests, pain points, and preferred social media platforms.

---

## Features
- **AI-Driven Analysis**:
  - Understand the essence of a company's brand, products, and goals.
  - Identify target audience demographics, interests, and pain points.
  - Determine preferred social media platforms for effective reach.
- **Tailored Marketing Strategies**:
  - Generate specific, actionable marketing strategies aligned with business goals.
  - Provide implementable steps for achieving marketing objectives.
- **Interactive UI**:
  - Accepts user input for company details, values, and goals.
  - Offers clear, actionable results for marketing planning.

---

## Installation

### Prerequisites
- **Python**: Ensure Python 3.8 or higher is installed.
- **Dependencies**: Install required packages via `requirements.txt`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/audience-navigator.git
   cd audience-navigator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your **OpenAI API Key**:
   - Create a `.streamlit/secrets.toml` file in the project directory.
   - Add your API key:
     ```toml
     [apikey]
     apikey = "your_openai_api_key"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## Usage

1. **Enter Company Details**: Input your company's name, core values, and goals into the text field.
2. **Generate Strategies**: Click the "OK" button to generate tailored marketing strategies and actionable steps.
3. **Review Results**: The app provides insights into audience demographics, interests, and preferred platforms, along with customized strategies.

---

## File Structure
```
audience-navigator/
│
├── app.py                  # Main application file
├── logo/                   # Contains app logo assets
│   ├── lyzr-logo.png
├── requirements.txt        # Python dependencies
└── .streamlit/             # Streamlit configuration
    └── secrets.toml        # API key configuration
```

---

## Key Functionalities

### 1. **Text Input**
- Accepts user-provided company information, values, and goals.

### 2. **AI-Powered Analysis**
- Uses GPT-4 to generate tailored marketing strategies and actionable insights.

### 3. **Custom Outputs**
- Provides actionable steps for audience engagement and achieving marketing goals.

---

## Dependencies
- **Streamlit**: Interactive UI framework.
- **Lyzr Automata SDK**: AI model integration for marketing strategy generation.
- **Pillow**: For handling image assets.
- **Python (>=3.8)**

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Acknowledgments
- Built with the **Lyzr Automata SDK**.
- Designed to simplify audience research and marketing strategy development.

---
