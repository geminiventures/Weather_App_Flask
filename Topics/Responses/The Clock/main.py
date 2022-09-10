from flask import Flask, make_response
import datetime

app = Flask('main')

@app.route('/')
def main_view():
    time = datetime.datetime.now()
    year, month, day = time.year, time.strftime('%m'), time.strftime('%d')
    request = make_response(f'{year}.{month}.{day}', 200)
    return request
