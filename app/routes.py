import requests

from flask import Flask, render_template, request
from app import app
#Needs app. AND foldername != filename (Context: We are idiots)
from app.helperFunctions.corona import getErlangen
import json



@app.route('/')
@app.route('/home')
def base():
    return render_template("home.html", user='Toby')

@app.route('/corona')
def corona():
    #x = requests.get('https://api.corona-zahlen.org/districts/09562').content
    # getErlangen()
    return render_template("corona.html", cor=getErlangen())

@app.route('/weather')
def weather():    
    
    #todo
    API_KEY_OPENWEATHER = ""

    url = 'http://api.openweathermap.org/data/2.5/weather?q=Erlangen&appid=' + API_KEY_OPENWEATHER

    response = requests.get(url)
    data = json.loads(response.text)
    return data
