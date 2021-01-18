import requests

def getErlangen():
    v_json = requests.get('https://api.corona-zahlen.org/districts/09562').content
    return v_json
