from flask import Flask
import requests

# For a random cat pic: https://cataas.com/cat

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    return response.content
