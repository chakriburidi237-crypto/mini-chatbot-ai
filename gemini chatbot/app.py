from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/country", methods=["POST"])
def country():
    try:
        data = request.get_json()
        country = data["country"]

        # Public country API
        url = f"https://restcountries.com/v3.1/name/{country}"

        response = requests.get(url)
        result = response.json()

        country_data = result[0]

        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["Unknown"])[0]
        region = country_data.get("region", "Unknown")
        population = country_data.get("population", "Unknown")

        specialities = f"""
• Capital: {capital}
• Region: {region}
• Population: {population}
• Famous Culture: Traditional festivals and heritage
• Tourist Attraction: Popular landmarks and natural beauty
"""

        return jsonify({
            "country": name,
            "specialities": specialities,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S")
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
