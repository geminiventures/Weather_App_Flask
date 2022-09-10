from flask import Flask

app = Flask('main')


@app.route("/about")
def render_about():
    return "Information about this page"


app.run()
