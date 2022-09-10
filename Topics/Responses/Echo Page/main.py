from flask import Flask, make_response

app = Flask('main')

@app.route('/<input_argument>')
def main_view(input_argument):
    response = make_response(input_argument, 204)
    return response