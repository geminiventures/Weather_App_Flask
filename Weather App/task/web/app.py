from flask import Flask, render_template, request, redirect, url_for, flash
import sys  # for __name__ == "__main__"
import requests  # pip install requests for working with external APIs
import math  # for converting kelvin to celsius math.floor()
#  import time  # work with Epoch time
from os import getenv  # pip install python-dotenv to load environment variables from .env file
from dotenv import load_dotenv  # pip install python-dotenv to hide API key
from city_database import CityDatabase  # import class from city_database.py

load_dotenv()  # load the API key from the .env file
app = Flask(__name__)
app.secret_key = getenv("DB_SECRET_KEY")
app.config.from_object('settings')  # load Flask settings from settings.py
db = CityDatabase()  # create an instance of the CityDatabase class

WEATHER_API_KEY = getenv("WEATHER_API_KEY")  # get the API key from environment variables


def convert_to_celsius(kelvin_value: float) -> float:
    return math.floor(kelvin_value - 273.15)


@app.route('/', methods=['GET'])
def index():
    all_cities = {}
    all_cities = db.get_cities()
    weather_data = {}
    for city, identity in all_cities.items():
        weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}')
        weather_city = weather.json()
        temp = convert_to_celsius(weather_city['main']['temp'])
        condition = weather_city['weather'][0]['main']
        city_name = city
        ident = f"/delete/{identity}"
        weather_data[city_name] = (temp, condition, ident)
    return render_template('index.html', weather_data=weather_data.items())


@app.route('/add', methods=['POST'])
def add_city():
    new_city = request.form['city_name']
    check_cities = db.get_cities()
    if new_city in check_cities.keys():
        flash("The city has already been added to the list!")
        return redirect(url_for('index'))
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={new_city}&appid={WEATHER_API_KEY}')
    weather_response = weather.json()
    if weather_response["cod"] == "400":
        flash("The city doesn't exist!")
        return redirect('/')
    elif weather_response["cod"] == "404":
        flash("The city doesn't exist!")
        return redirect('/')
    else:
        db.add_city(new_city)
        return redirect(url_for('index'))
    # db_response = db.add_city(new_city)
    # if db_response == "CITY_EXISTS":


@app.route('/delete/<city_id>', methods=['POST', 'GET'])
def delete(city_id):
    db.delete_city(city_id)
    return redirect('/')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()

# figure out if it is day or night
# def time_of_day(weather_object):
#     current_time = int(time.localtime(int(weather_object["dt"]))[3])
#     sunrise = int(time.localtime(int(weather_object["sys"]["sunrise"]))[3])
#     sunset = int(time.localtime(int(weather_object["sys"]["sunset"]))[3])
#     if current_time >= sunrise and current_time < sunset:
#         return "card day"
#     elif current_time >= sunset and current_time < sunrise:
#         return "card night"
