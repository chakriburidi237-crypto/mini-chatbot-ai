<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3c72,100:2a5298&height=200&section=header&text=Mini%20Chatbot%20AI&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Country%20Guide%20%7C%20Flask%20%2B%20REST%20API%20%7C%20Real-Time%20Chat%20UI&descAlignY=55&descSize=17" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-green?style=for-the-badge&logo=api&logoColor=white)

<br/>

> ### 🌍 *"Ask any country — get instant AI-powered insights"*
> **Flask Backend • Live REST API • Animated Chat UI • Real-Time Data**

<br/>

![Visitor Count](https://komarev.com/ghpvc/?username=chakriburidi237-crypto&color=2a5298&style=flat-square&label=Profile+Views)

---

</div>

## 🎯 What Is This Project?

**Mini Chatbot AI** is an AI-powered conversational chatbot that provides real-time country information using a live REST API. Built with a **Flask backend**, **Vanilla JavaScript frontend**, and integrated with the **REST Countries public API**.

Type any country name → Get instant details including capital, region, population, culture and tourist attractions — all inside a clean, animated chat interface.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 **Country Search** | Search any country by name instantly |
| 📡 **Live API Data** | Fetches real-time data from REST Countries API |
| 💬 **Chat Interface** | Smooth, animated chatbot-style conversation UI |
| ⌨️ **Typing Indicator** | "Bot is typing..." animation while fetching |
| ⏱️ **Timestamp** | Each response shows date and time |
| ⌨️ **Enter Key Support** | Press Enter to search — no click needed |
| 🎨 **Animated Messages** | Fade-in animation for every chat message |
| 📱 **Clean Design** | Glassmorphism-inspired card with gradient background |

---

## 🏗️ Project Structure

```
mini-chatbot-ai-main/
│
└── gemini chatbot/
    ├── app.py                  # Flask backend + REST API integration
    ├── requirements.txt        # Python dependencies
    │
    ├── templates/
    │   └── index.html          # Main HTML chat interface
    │
    └── static/
        ├── script.js           # Async JavaScript (fetch API + DOM)
        └── style.css           # Chat UI styling + animations
```

---

## 🔌 How It Works

```
User types country name
        ↓
JavaScript sends POST request to /country
        ↓
Flask receives request
        ↓
Calls REST Countries API (restcountries.com)
        ↓
Extracts: Name, Capital, Region, Population
        ↓
Returns JSON response with timestamp
        ↓
JavaScript renders animated chat message
```

---

## 🌐 API Integration

### External API Used:
**REST Countries API** — `https://restcountries.com/v3.1/name/{country}`

### Flask Endpoint:

```python
@app.route("/country", methods=["POST"])
def country():
    data = request.get_json()
    country = data["country"]
    
    # Fetch from REST Countries API
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    result = response.json()
    
    # Extract key info
    name    = country_data["name"]["common"]
    capital = country_data.get("capital", ["Unknown"])[0]
    region  = country_data.get("region", "Unknown")
    population = country_data.get("population", "Unknown")
    
    return jsonify({
        "country": name,
        "specialities": specialities,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S")
    })
```

### Example Response:

```json
{
  "country": "India",
  "specialities": "• Capital: New Delhi\n• Region: Asia\n• Population: 1380004385\n• Famous Culture: Traditional festivals and heritage\n• Tourist Attraction: Popular landmarks and natural beauty",
  "date": "2026-03-01",
  "time": "14:32:10"
}
```

---

## 🎨 Frontend — Chat UI

### JavaScript (Async Fetch):
```javascript
async function sendMessage() {
    const response = await fetch("/country", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ country: country })
    });
    const data = await response.json();
    // Renders animated chat bubble with country info
}
```

### CSS Animations:
```css
.message {
    animation: fadeIn 0.4s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python + Flask | REST API server & routing |
| **API Integration** | requests library | Fetch live country data |
| **Frontend** | HTML5 + CSS3 | Chat interface structure & styling |
| **Logic** | Vanilla JavaScript | Async fetch, DOM manipulation |
| **Data Source** | REST Countries API | Real-time country information |
| **Styling** | CSS3 Animations | Fade-in message effects |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip
- Internet connection (for REST Countries API)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/chakriburidi237-crypto/mini-chatbot-ai.git
cd mini-chatbot-ai/gemini\ chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
flask
google-generativeai
```

### Run the App

```bash
python app.py
```

Open your browser at: **`http://127.0.0.1:5000`** 🎉

---

## 💬 Usage

```
1. Open http://127.0.0.1:5000 in your browser
2. Type any country name in the input box
   Example: "India", "Japan", "Brazil", "France"
3. Press Enter or click Search
4. See the bot reply with country details instantly!
```

### Sample Conversation:
```
You:  India
Bot:  Specialities of India:
      • Capital: New Delhi
      • Region: Asia
      • Population: 1,380,004,385
      • Famous Culture: Traditional festivals and heritage
      • Tourist Attraction: Popular landmarks and natural beauty
      2026-03-01  14:32:10
```

---

## 📸 UI Preview

```
┌─────────────────────────────────────────┐
│  🌍 AI Country Specialities Guide        │
├─────────────────────────────────────────┤
│                                         │
│  [You]: India              ──────────►  │
│                                         │
│  ◄──── Bot is typing...                 │
│                                         │
│  ◄──── Specialities of India:           │
│        • Capital: New Delhi             │
│        • Region: Asia                   │
│        • Population: 1.38B              │
│        2026-03-01  14:32:10             │
│                                         │
├─────────────────────────────────────────┤
│  [Enter country name...]    [Search]    │
└─────────────────────────────────────────┘
```

---

## 🔮 Future Improvements

- [ ] 🤖 Integrate Google Gemini AI for richer, conversational responses
- [ ] 🗺️ Add country flag display using API flag URLs
- [ ] 📊 Show population chart with Chart.js
- [ ] 🌐 Add multi-language support
- [ ] 💾 Save chat history to localStorage
- [ ] 📱 Make fully mobile responsive
- [ ] 🔍 Add autocomplete suggestions for country names
- [ ] 🌙 Add dark mode toggle

---

## 👨‍💻 Developer

<div align="center">

**Surya Chakradhar Buridi**

*AI/ML Engineer | Flask & Python Developer*
*B.E. Artificial Intelligence & Machine Learning @ KIET*
*Ex-Industrial Trainee @ Schneider Electric, Bengaluru*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/surya-chakradhar-buridi-767548355)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chakriburidi237-crypto)

</div>

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3c72,100:2a5298&height=200&section=header&text=Mini%20Chatbot%20AI&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Country%20Guide%20%7C%20Flask%20%2B%20REST%20API%20%7C%20Real-Time%20Chat%20UI&descAlignY=55&descSize=17" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-green?style=for-the-badge&logo=api&logoColor=white)

<br/>

> ### 🌍 *"Ask any country — get instant AI-powered insights"*
> **Flask Backend • Live REST API • Animated Chat UI • Real-Time Data**

<br/>

![Visitor Count](https://komarev.com/ghpvc/?username=chakriburidi237-crypto&color=2a5298&style=flat-square&label=Profile+Views)

---

</div>

## 🎯 What Is This Project?

**Mini Chatbot AI** is an AI-powered conversational chatbot that provides real-time country information using a live REST API. Built with a **Flask backend**, **Vanilla JavaScript frontend**, and integrated with the **REST Countries public API**.

Type any country name → Get instant details including capital, region, population, culture and tourist attractions — all inside a clean, animated chat interface.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌍 **Country Search** | Search any country by name instantly |
| 📡 **Live API Data** | Fetches real-time data from REST Countries API |
| 💬 **Chat Interface** | Smooth, animated chatbot-style conversation UI |
| ⌨️ **Typing Indicator** | "Bot is typing..." animation while fetching |
| ⏱️ **Timestamp** | Each response shows date and time |
| ⌨️ **Enter Key Support** | Press Enter to search — no click needed |
| 🎨 **Animated Messages** | Fade-in animation for every chat message |
| 📱 **Clean Design** | Glassmorphism-inspired card with gradient background |

---

## 🏗️ Project Structure

```
mini-chatbot-ai-main/
│
└── gemini chatbot/
    ├── app.py                  # Flask backend + REST API integration
    ├── requirements.txt        # Python dependencies
    │
    ├── templates/
    │   └── index.html          # Main HTML chat interface
    │
    └── static/
        ├── script.js           # Async JavaScript (fetch API + DOM)
        └── style.css           # Chat UI styling + animations
```

---

## 🔌 How It Works

```
User types country name
        ↓
JavaScript sends POST request to /country
        ↓
Flask receives request
        ↓
Calls REST Countries API (restcountries.com)
        ↓
Extracts: Name, Capital, Region, Population
        ↓
Returns JSON response with timestamp
        ↓
JavaScript renders animated chat message
```

---

## 🌐 API Integration

### External API Used:
**REST Countries API** — `https://restcountries.com/v3.1/name/{country}`

### Flask Endpoint:

```python
@app.route("/country", methods=["POST"])
def country():
    data = request.get_json()
    country = data["country"]
    
    # Fetch from REST Countries API
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    result = response.json()
    
    # Extract key info
    name    = country_data["name"]["common"]
    capital = country_data.get("capital", ["Unknown"])[0]
    region  = country_data.get("region", "Unknown")
    population = country_data.get("population", "Unknown")
    
    return jsonify({
        "country": name,
        "specialities": specialities,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S")
    })
```

### Example Response:

```json
{
  "country": "India",
  "specialities": "• Capital: New Delhi\n• Region: Asia\n• Population: 1380004385\n• Famous Culture: Traditional festivals and heritage\n• Tourist Attraction: Popular landmarks and natural beauty",
  "date": "2026-03-01",
  "time": "14:32:10"
}
```

---

## 🎨 Frontend — Chat UI

### JavaScript (Async Fetch):
```javascript
async function sendMessage() {
    const response = await fetch("/country", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ country: country })
    });
    const data = await response.json();
    // Renders animated chat bubble with country info
}
```

### CSS Animations:
```css
.message {
    animation: fadeIn 0.4s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python + Flask | REST API server & routing |
| **API Integration** | requests library | Fetch live country data |
| **Frontend** | HTML5 + CSS3 | Chat interface structure & styling |
| **Logic** | Vanilla JavaScript | Async fetch, DOM manipulation |
| **Data Source** | REST Countries API | Real-time country information |
| **Styling** | CSS3 Animations | Fade-in message effects |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip
- Internet connection (for REST Countries API)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/chakriburidi237-crypto/mini-chatbot-ai.git
cd mini-chatbot-ai/gemini\ chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
flask
google-generativeai
```

### Run the App

```bash
python app.py
```

Open your browser at: **`http://127.0.0.1:5000`** 🎉

---

## 💬 Usage

```
1. Open http://127.0.0.1:5000 in your browser
2. Type any country name in the input box
   Example: "India", "Japan", "Brazil", "France"
3. Press Enter or click Search
4. See the bot reply with country details instantly!
```

### Sample Conversation:
```
You:  India
Bot:  Specialities of India:
      • Capital: New Delhi
      • Region: Asia
      • Population: 1,380,004,385
      • Famous Culture: Traditional festivals and heritage
      • Tourist Attraction: Popular landmarks and natural beauty
      2026-03-01  14:32:10
```

---

## 📸 UI Preview

```
┌─────────────────────────────────────────┐
│  🌍 AI Country Specialities Guide        │
├─────────────────────────────────────────┤
│                                         │
│  [You]: India              ──────────►  │
│                                         │
│  ◄──── Bot is typing...                 │
│                                         │
│  ◄──── Specialities of India:           │
│        • Capital: New Delhi             │
│        • Region: Asia                   │
│        • Population: 1.38B              │
│        2026-03-01  14:32:10             │
│                                         │
├─────────────────────────────────────────┤
│  [Enter country name...]    [Search]    │
└─────────────────────────────────────────┘
```

---

## 🔮 Future Improvements

- [ ] 🤖 Integrate Google Gemini AI for richer, conversational responses
- [ ] 🗺️ Add country flag display using API flag URLs
- [ ] 📊 Show population chart with Chart.js
- [ ] 🌐 Add multi-language support
- [ ] 💾 Save chat history to localStorage
- [ ] 📱 Make fully mobile responsive
- [ ] 🔍 Add autocomplete suggestions for country names
- [ ] 🌙 Add dark mode toggle

---

## 👨‍💻 Developer

<div align="center">

**Surya Chakradhar Buridi**

*AI/ML Engineer | Flask & Python Developer*
*B.E. Artificial Intelligence & Machine Learning @ KIET*
*Ex-Industrial Trainee @ Schneider Electric, Bengaluru*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/surya-chakradhar-buridi-767548355)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/chakriburidi237-crypto)

</div>

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2a5298,100:1e3c72&height=100&section=footer" width="100%"/>

**⭐ Found this useful? Give it a star!**

*Built with ❤️ by Surya Chakradhar Buridi*
*Associated with Kakinada Institute of Engineering and Technology (KIET)*

</div>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2a5298,100:1e3c72&height=100&section=footer" width="100%"/>

**⭐ Found this useful? Give it a star!**

*Built with ❤️ by Surya Chakradhar Buridi*
*Associated with Kakinada Institute of Engineering and Technology (KIET)*

</div>
