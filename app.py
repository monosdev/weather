import json, sys, os, requests

def get_resource():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return base_path

config_path = os.path.join(get_resource(), 'config.json')

with open(config_path) as file:
    config = json.load(file)

api_key = config.get('api_key')
if not api_key:
    print("Api key is missing.")
    exit(1)

while True:
    location = input('Location: ')
    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}')

    if result.json()['cod'] == '404':
        print('Invalid location!')
        continue
    break

description = result.json()['weather'][0]['description']
temperature = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
high = round(result.json()['main']['temp_max'])
low = round(result.json()['main']['temp_min'])

print(f"The weather in {location[0].upper()}{location[1:]} is {temperature} °C with {description}.")
print(f"It feels like {feels_like} °C.")
print(f"Today's high is {high} °C and today's low is {low} °C.")