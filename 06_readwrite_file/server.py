from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        country = request.form["country"]
        fh = open("data.txt", "a")
        fh.writelines(country + "\n")
        fh.close()

    countries = []
    fh = open("data.txt", "r")
    for country in fh.readlines():
        countries.append(country)
    fh.close()
        
    return render_template('index.html', countries=countries)   
