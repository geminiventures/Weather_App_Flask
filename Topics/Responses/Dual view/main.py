from flask import Flask, make_response

app = Flask('main')


@app.route('/data/main_info')
def view_func1():
    response = make_response("<h1>Hello there, it's me — my own worst enemy!</h1>", 200)
    return response



@app.route('/the_wall')
def view_func2():
    response = make_response("<h1>Welkommen!</h1>", 200)
    return response

