<h1 align="center">💧 WaterAI</h1>
<p align="center">
A web-based AI assistant for analyzing water quality data using Google Gemini.
<br/>
<em>Designed to support SDG 6: Clean Water and Sanitation</em>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11+-blue?logo=python">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-Microframework-black?logo=flask">
  <img alt="Gemini API" src="https://img.shields.io/badge/Gemini%20API-Google%20LLM-red?logo=google">
  <img alt="License" src="https://img.shields.io/github/license/yourusername/WaterAI">
  <img alt="Status" src="https://img.shields.io/badge/Status-Working-success">
</p>

---

## 📌 Overview

**WaterAI** is a lightweight web application that uses the **Gemini AI API** to analyze water quality parameters based on WHO standards. With a modern UI and intelligent backend, it delivers:

- Overall water quality assessment
- Risk level estimation
- Recommendations and solutions
- SDG 6 alignment

All of this — through a **single-page interface** and a **Flask backend**.

---

## 🧠 Features

- 📊 Real-time water data input and visualization
- 🧪 AI-driven water quality analysis
- ⚠️ Detection of key issues and health risks
- 💡 Actionable short/long-term solutions
- 🎯 SDG 6 (Clean Water and Sanitation) alignment
- 🌗 Fully responsive dark/light theme switcher

---

## 🛠 Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| 🧠 AI Engine  | [Google Gemini](https://ai.google.dev/) |
| ⚙️ Backend    | Flask + Python 3.11            |
| 🌐 Frontend   | HTML5, CSS3, Vanilla JS        |
| 🌍 Hosting    | Render / Localhost             |

---

## 📁 Project Structure

```

WaterAI/
├── app.py                 # Flask backend + Gemini integration
├── templates/
│   └── index.html         # Frontend form UI
├── .env                   # API key (not committed)
├── requirements.txt       # Python dependencies
└── README.md              # You're reading it

````

---

## ⚙️ Setup Instructions

### 🔐 Prerequisites

- Python 3.11+
- A free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

---

### 🧪 Local Installation

```bash
# 1. Clone the repository
git clone https://github.com/Ishan0121/WaterAI.git
cd WaterAI

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file and add your Gemini API key
echo "GEMINI_API_KEY=your_google_gemini_api_key" > .env

# 5. Run the application
python app.py
````

Visit `http://localhost:5000` in your browser.

---

## 🚀 Deployment

### 🌐 Deploy to Render

1. Push this repo to GitHub
2. Create a [Render Web Service](https://render.com/)
3. Add your `GEMINI_API_KEY` as an environment variable
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python app.py`

---

## 📊 Demo Preview

> *(Insert a GIF or screenshot here of the form + results)*
> I can help you create one if you want it polished.

---

## 🧠 AI Prompt Logic

The backend sends structured water quality data to Gemini using a prompt that:

* Analyzes parameters against WHO standards
* Expects structured JSON in return
* Extracts key insights: quality, risks, solutions, SDG alignment

The Gemini response is parsed and visualized in a well-designed UI.

---

## ✅ Sample Output

```json
{
  "quality_assessment": "Fair",
  "risk_level": "Medium",
  "key_issues": ["High turbidity", "Low pH level"],
  "short_term_solutions": ["Install local filtration units"],
  "long_term_solutions": ["Build community water treatment plant"],
  ...
}
```

---

## 📑 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

---

## 🤝 Contributing

Pull requests are welcome. If you'd like to add a feature, create an issue first.

---

<!-- ## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

--- -->

## 🌍 SDG Alignment

WaterAI is built to support:

* **6.1** – Safe and affordable drinking water
* **6.3** – Improve water quality, reduce pollution
* **6.B** – Community participation in water management

---

## 🧬 Future Plans

* [ ] Support for CSV batch analysis
* [ ] Multilingual support
* [ ] Mobile PWA support
* [ ] LLM fallback using Ollama or GPT-4

---

<p align="center">
  Built with ❤️ by <b>Me</b> | 2025
</p>