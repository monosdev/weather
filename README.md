# Weather
Check your local weather forecast

A command-line Python app that fetches real-time weather data for any city using the OpenWeatherMap API.

## ✨ Features

- Get current temperature (°C)
- See weather conditions (sunny, rainy, cloudy, etc.)
- Check humidity and wind speed
- Works for any city worldwide
- Color-coded output for easy reading



## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Libraries:** `requests`, `python-dotenv`
- **API:** [OpenWeatherMap](https://openweathermap.org/api)

## 🚀 Getting Started

### Prerequisites

Before running this app, make sure you have:
- Python 3.10 or higher installed
- A free API key from [OpenWeatherMap](https://openweathermap.org)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/console-weather-app.git
cd console-weather-app
```

2. Install the required libraries:

```bash
pip install requests python-dotenv
```

3. Create a `.env` file in the project root and add your API key:

```
API_KEY=your_openweathermap_api_key_here
```



### Running the App

```bash
python weather.py
```

## 📸 Demo

```
Enter city name: London

📍 Weather in London, GB
━━━━━━━━━━━━━━━━━━━━━━━
🌡️  Temperature : 14°C
🌥️  Condition   : Overcast clouds
💧 Humidity    : 78%
💨 Wind Speed  : 5.2 m/s
━━━━━━━━━━━━━━━━━━━━━━━
```



## 🗺️ Roadmap

Planned features for future versions:
- [ ] 5-day weather forecast
- [ ] Save favorite cities
- [ ] Weather alerts for extreme conditions
- [ ] ASCII weather art based on conditions

## 📚 What I Learned

Building this project taught me how to:
- Make HTTP requests to a real-world API using Python
- Parse and work with JSON data
- Manage secret keys safely using environment variables
- Structure a Python project with clean, readable code



## 📄 License

This project is licensed under the [MIT License](LICENSE).

---
Made with ☕ by [Your Name](https://github.com/your-username)