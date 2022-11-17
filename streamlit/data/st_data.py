import requests

url = "http://0.0.0.0:8000"

def get_total_immigrants():
    return requests.get(url + "/totalimmigrants/{neighborhood}").json()

def get_total_unemployed():
    return requests.get(url + "/totalunemployed/{neighborhood}").json()

def get_total():
    return requests.get(url + "/totalpopulation/{neighborhood}").json()
