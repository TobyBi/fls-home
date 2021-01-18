import requests
import json


from flask import Flask, render_template, request
from app import app
from decouple import config


#Needs app. AND foldername != filename (Context: We are idiots)
from app.helperFunctions.corona import getErlangen
from app.some_static_shit import *



@app.route('/')
@app.route('/home')
def base():
    return render_template("home.html", user='Toby')

@app.route('/corona')
def corona():
    y = requests.get('https://api.corona-zahlen.org/districts/' + CITY_CODE)
    y = y.json()
    return {
        'data': y['data'][CITY_CODE],
        'meta': y['meta'],
    }
    return render_template("corona.html", cor=y['meta']['contact'])

@app.route('/weather')
def weather():    
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Erlangen&appid=' + config('KEY_API_OPENWEATHERMAP')
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.route('/test')
def test():
    return
