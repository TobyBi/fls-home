import requests

x = 19


def getErlangen():
    return requests.get('https://api.corona-zahlen.org/districts/09562').content
