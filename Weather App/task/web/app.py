from flask import Flask, render_template, request
import sys # for __name__ == "__main__"
import requests # pip install requests for working with external APIs
import math # for converting kelvin to celsius math.floor()
import time # work with Epoch time
from os import getenv # pip install python-dotenv to load environment variables from .env file
from dotenv import load_dotenv # pip install python-dotenv to hide API key

load_dotenv() # load the API key from the .env file


WEATHER_API_KEY = getenv("WEATHER_API_KEY") # get the API key from environment variables


def convert_to_celcius(kelvin_value: float) -> float:
    return math.floor(kelvin_value - 273.15)

# figure out if it is day or night
def time_of_day(weather_object):
    current_time = int(time.localtime(int(weather_object["dt"]))[3])
    sunrise = int(time.localtime(int(weather_object["sys"]["sunrise"]))[3])
    sunset = int(time.localtime(int(weather_object["sys"]["sunset"]))[3])
    if current_time >= sunrise and current_time < sunset:
        return "card day"
    elif current_time > sunset and current_time < sunrise:
        return "card night"



app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def get_weather():
    city = request.form['city_name']
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}')
    weather_city = weather.json()
    temp = convert_to_celcius(weather_city['main']['temp'])
    condition = weather_city['weather'][0]['main']
    card_selection = time_of_day(weather_city)
    return render_template('index.html', temp=temp, condition=condition, city=city, weather_city=weather_city,
                           card_selection=card_selection)


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
