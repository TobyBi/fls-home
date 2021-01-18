from flask import render_template
import requests
from app import app
#Needs app. AND foldername != filename (Context: We are idiots)
from app.helperFunctions.corona import getErlangen



@app.route('/')
@app.route('/home')
def base():
    return render_template("home.html", user='Toby')

@app.route('/corona')
def corona():
    #x = requests.get('https://api.corona-zahlen.org/districts/09562').content
    # getErlangen()
    return getErlangen()
