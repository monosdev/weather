# Weather

English | 正體中文

A command-line Python app that fetches real-time weather data for any city using the [OpenWeatherMap](https://openweathermap.org/) API.

## Features

- Get current temperature (°C)
- See weather conditions (sunny, rainy, cloudy, etc.)
- Check high and low temperature
- Works for any city worldwide

## Installation

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

## Running

```bash
python weather.py
```

## Demo



## Roadmap

Planned features for future versions:
- [ ] 5-day weather forecast
- [ ] Save favorite cities
- [ ] Weather alerts for extreme conditions
- [ ] ASCII weather art based on conditions

## License

This project is licensed under the [MIT License](./LICENSE).