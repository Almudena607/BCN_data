import requests

def neighborhoods_data(neighborhoods):
    return requests.get("http://localhost:8000/neighborhoods{neighborhoods}").json()

  
