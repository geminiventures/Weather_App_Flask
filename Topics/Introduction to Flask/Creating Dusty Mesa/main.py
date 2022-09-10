from flask import Flask

app = Flask('super-app')

@app.route('/')
def index():
    return "From the dusty mesa, her looming shadow grows..."