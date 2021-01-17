from flask import render_template

from app import app

@app.route('/')
@app.route('/home')
def base():
    return render_template("home.html", user='Toby')

@app.route('/corona')
def corona():
    return render_template("corona.html")