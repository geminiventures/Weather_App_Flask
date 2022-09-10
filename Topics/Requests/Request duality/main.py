from flask import Flask, request

app = Flask('main')

@app.route('/', methods=['GET', 'POST'])
def main_view():
    if request.method == 'GET':
        return "I'm GETting some diamonds..."
    elif request.method == 'POST':
        return "Hey, there is an imPOSTor!"
    return None