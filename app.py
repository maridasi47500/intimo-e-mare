from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>&#128089; &#129652; &#x1fa71; &#x1f457;</p>"
