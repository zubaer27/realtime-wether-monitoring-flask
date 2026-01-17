from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "da5802c5db817302f4c34cecf0d17bbd"   # অবশ্যই নিজের key বসাবে
CITY = "Dhaka"

@app.route("/")
def home():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    # যদি ঠিক ডাটা না আসে
    if "main" not in data:
        return f"API Problem: {data}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"Weather in {CITY}: {temp}°C, {desc}"

if __name__ == "__main__":
    app.run(debug=False)
