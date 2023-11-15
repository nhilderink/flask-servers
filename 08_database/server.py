import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://site:E1ZwYVCqS.]Z1Dyu@134.122.62.11:3306/shop"
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'PRODUCTS'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer)

@app.route("/")
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route("/product/<int:id>")
def product(id):
    product = Product.query.get(id)
    return render_template('wiet.html', product=product)

@app.route("/forum.html")
def forum():
    return render_template('forum.html')

@app.route("/sitemap.xml")
def sitemap():
    return render_template('sitemap.xml')

@app.route("/feed.rss")
def feed():
    return render_template('feed.rss')

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')
