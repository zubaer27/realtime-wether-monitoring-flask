from flask import Flask
import requests
import os

app = Flask(__name__)

API_KEY = "da5802c5db817302f4c34cecf0d17bbd"
CITY = "Dhaka"

@app.route("/")
def home():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    if "main" not in data:
        return f"API Error: {data}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"Weather in {CITY}: {temp}°C, {desc}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
