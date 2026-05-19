# 🌤️ Real-Time Weather App
A simple, fast, and beautiful weather application built with Python and Flask. This app fetches real-time weather data from the OpenWeatherMap API to display the current temperature, weather conditions, humidity, and wind speed for any city worldwide.

## ✨ Features
* **Real-Time Data:** Fetches live weather updates via the OpenWeatherMap API.
* **Glassmorphism UI:** Clean, modern, and semi-transparent user interface.
* **Dynamic Icons:** Displays official weather icons matching the current conditions.
* **Error Handling:** Gracefully handles invalid city names or API errors.

## 🛠️ Tech Stack
* **Backend:** Python, Flask Framework, Requests Library
* **Frontend:** HTML5, CSS3
* **API:** OpenWeatherMap API

## 📸 App Screenshot
*(You can drop your screenshot image here later)*

## 🚀 How to Run Locally
1. Clone this repository: `git clone https://github.com/gustisuryaa/weather-app.git`
2. Navigate to the project directory: `cd weather-app`
3. Create and activate a virtual environment:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. **API Key Setup (Important):**
   - Create a free account at [OpenWeatherMap](https://openweathermap.org/) and get your API Key.
   - Open `app.py` and replace the placeholder with your actual API key.
6. Run the application: `python app.py`
7. Open your browser and go to `http://127.0.0.1:5000`