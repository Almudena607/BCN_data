import requests

STURL="http://localhost:8000"

#selectboxes
def all_nationality():
    return requests.get(STURL + "/nationality/all").json()

def all_district():
    return requests.get(STURL + "/district/all").json()

def all_neigh():
    return requests.get(STURL + "/neighborhood/all").json()


#immigrants
def get_immigrants_neighborhood(district, num_page):
    return requests.get(STURL + f"/district/immigrants/{district}/{num_page}").json()

def get_immigrants_nationality(nationality, num_page):
    return requests.get(STURL + f"/nationality/immigrants/{nationality}/{num_page}").json()


#unemployment
def get_unemployed_neighborhood(district, num_page):
    return requests.get(STURL + f"/district/unemployment/{district}/{num_page}").json()

#population
def get_population_neighborhood(district, num_page):
    return requests.get(STURL + f"/district/population/{district}/{num_page}").json()

#total
def get_neighborhoods(num_page):
    return requests.get(STURL + f"/neighborhoods/{num_page}").json()
    
def get_total_immigrants(neighborhood):
    return requests.get(STURL + f"/totalimmigrants/{neighborhood}").json()

def get_total_unemployed(neighborhood):
    return requests.get(STURL + f"/totalunemployed/{neighborhood}").json()

def get_total(neighborhood):
    return requests.get(STURL + f"/totalpopulation/{neighborhood}").json()


def immigrants_nationality(nationality):
    return requests.get(STURL + f"/nationality/immigrants/{nationality}").json()

