from flask import Flask, render_template, request, jsonify
import os
import requests
from datetime import datetime

app = Flask(__name__)

# Optional Google Gemini AI initialization
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
gemini_model = None
if GEMINI_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_KEY)
        gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    except Exception as e:
        print(f"Gemini initialization note: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/country", methods=["POST"])
def country():
    try:
        data = request.get_json() or {}
        country_name = data.get("country", "").strip()

        if not country_name:
            return jsonify({"error": "Please provide a valid country name."}), 400

        # Public REST Countries API
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url, timeout=5)
        
        capital = "Information Unavailable"
        region = "Global"
        population = "Unknown"
        currencies = "Local Currency"
        languages = "Multiple"
        resolved_name = country_name.title()

        if response.status_code == 200:
            result = response.json()
            if result and isinstance(result, list):
                country_data = result[0]
                resolved_name = country_data.get("name", {}).get("common", country_name.title())
                capital = country_data.get("capital", ["Information Unavailable"])[0]
                region = country_data.get("region", "Global")
                pop_val = country_data.get("population")
                population = f"{pop_val:,}" if isinstance(pop_val, (int, float)) else str(pop_val)
                
                curr_dict = country_data.get("currencies", {})
                if curr_dict:
                    currencies = ", ".join([v.get("name", k) for k, v in curr_dict.items()])
                    
                lang_dict = country_data.get("languages", {})
                if lang_dict:
                    languages = ", ".join(lang_dict.values())

        # Gemini AI insight enhancement if available
        ai_insight = None
        if gemini_model:
            try:
                prompt = (
                    f"Provide 2 concise, fascinating cultural highlights and 1 signature culinary specialty "
                    f"of {resolved_name} in 3 bullet points."
                )
                ai_resp = gemini_model.generate_content(prompt)
                if ai_resp and ai_resp.text:
                    ai_insight = ai_resp.text.strip()
            except Exception:
                ai_insight = None

        if not ai_insight:
            ai_insight = (
                f"• Famous Heritage: Celebrated for its distinct cultural identity and historical landmarks.\n"
                f"• Geography & Society: Vibrant communities situated across the {region} region.\n"
                f"• Gastronomy: Rich traditional culinary staples and authentic regional delicacies."
            )

        specialities = f"""• Capital: {capital}
• Region: {region}
• Population: {population}
• Languages: {languages}
• Currency: {currencies}

{ai_insight}"""

        return jsonify({
            "country": resolved_name,
            "specialities": specialities,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S")
        })

    except Exception as e:
        return jsonify({"error": f"Failed to retrieve details: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
