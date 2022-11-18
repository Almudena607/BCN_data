import requests

STURL="http://localhost:8000"

def get_neighborhoods():
    return requests.get(STURL + "/neighborhoods").json
    
def get_total_immigrants(neighborhood):
    return requests.get(STURL + f"/totalimmigrants/{neighborhood}").json()

def get_total_unemployed(neighborhood):
    return requests.get(STURL + f"/totalunemployed/{neighborhood}").json()

def get_total(neighborhood):
    return requests.get(STURL + f"/totalpopulation/{neighborhood}").json()

def all_neigh():
    return requests.get(STURL + "/neighborhood/all").json()

def immigrants_nationality(nationality):
    return requests.get(STURL + f"/nationality/immigrants/{nationality}").json()