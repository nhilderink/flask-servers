from flask import Flask
from flask import render_template, make_response, request

app = Flask(__name__)

@app.route("/")
def index():
    cookie = None
    if request.cookies.get('cookie'):
        cookie = request.cookies.get('cookie')
    return render_template('index.html', cookie=cookie)


@app.route("/cookie")
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('cookie', 'Hello Cookie!')
    return response
