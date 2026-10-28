# Mini Chatbot AI (AI Country Guide)

> **"Explore the World. Discover Cultures. Powered by AI & Global Telemetry."**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-black.svg)](https://flask.palletsprojects.com/)
[![Gemini AI](https://img.shields.io/badge/Google_Gemini-1.5_Flash-8E75C2.svg)](https://ai.google.dev/)

Mini Chatbot AI is an interactive conversational travel assistant and global knowledge engine. Built with a lightweight Flask backend and animated modern web frontend, it allows users to discover key demographic telemetry, economic currencies, official languages, and AI-curated cultural highlights for any nation on Earth. It integrates the REST Countries API with Google Gemini AI (`gemini-1.5-flash`), featuring seamless offline fallback capabilities.

---

## 🚀 Key Features

1. **Dual-Intelligence Knowledge Retrieval**: Combines real-time demographic and geographic facts from authoritative public registries with generative cultural summaries powered by Google Gemini.
2. **Resilient Zero-Config Fallback**: Fully functional out of the box even without an API key! If Gemini AI is unconfigured or rate-limited, the system falls back to structured geographical profiles automatically.
3. **Instant Real-Time Chat Experience**: Responsive single-page interface with typing indicators, animated message entrance transitions, and automatic bottom-scrolling.
4. **Rich Country Fact Sheets**: Surfaces country capitals, geographic regions, census population counts, circulating currencies, and predominant spoken languages.
5. **Lightweight & Cloud-Deployable**: Minimal dependency footprint engineered for instant deployment on PaaS platforms (Render, Railway, Heroku) or containerized microservices.

---

## 🛠 Tech Stack

- **Backend**: Python 3.10+, Flask
- **AI Integration**: Google Gemini (`google-generativeai`)
- **External Data**: REST Countries API (HTTPS JSON endpoint)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3 with responsive card layouts and CSS animations
- **Testing**: Pytest with Flask test client fixtures

---

## 🏗 Architecture & Directory Structure

```
mini-chatbot-ai/
├── static/
│   ├── script.js             # Client-side messaging and DOM renderer
│   └── style.css             # Gradient background and chat styling
├── templates/
│   └── index.html            # Main single-page application layout
├── tests/
│   └── test_app.py           # Automated route and API validation tests
├── app.py                    # Flask application, routing, and Gemini integration
├── requirements.txt          # Python runtime dependencies
├── .env.example              # Environment variable template
├── .gitattributes            # Linguist rules for accurate language attribution
├── .gitignore                # Ignored virtualenvs and cache files
├── LICENSE                   # MIT License
└── README.md                 # Project documentation
```

---

## ⚡ Getting Started

### Prerequisites

- Python `3.10` or higher
- `pip` package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/chakriburidi237-crypto/mini-chatbot-ai.git
   cd mini-chatbot-ai
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Configure Gemini API Key:
   ```bash
   cp .env.example .env
   ```
   Add your key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   *(Note: The chatbot functions smoothly even without an API key using built-in geographical telemetry).*

5. Run the web application:
   ```bash
   python app.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

---

## 🧪 Automated Testing

Execute the test suite to verify route response status, error handling, and payload schemas:

```bash
pytest tests/ -v
```

Expected output:
```
tests/test_app.py::test_home_page PASSED
tests/test_app.py::test_country_endpoint_missing_payload PASSED
tests/test_app.py::test_country_endpoint_valid PASSED
======================== 3 passed in 0.52s ========================
```

---

## 🚀 Deployment

### Deploy to Render / Railway

1. Connect your repository to [Render](https://render.com).
2. Set Build Command: `pip install -r requirements.txt`
3. Set Start Command: `gunicorn app:app` or `python app.py`
4. Set Environment Variables:
   - `GEMINI_API_KEY` (Optional)

---

## 📄 License and Copyright\n\nAll rights reserved © 2026 Chakradhar Buridi.

