import requests
import json

def getAuthToken():
    headers = {'Authorization': 'Basic MWUzMTIzMmMzMjMwNDIzZGI3M2.....WY6NDhiZTNhMzIyMjYwNDI0MThkNThkY2RkZWJmMTQ4ZTU=',}
    data = {'grant_type': 'client_credentials'}
    r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    if r.status_code == 200:
        return r.json()["access_token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

print(getAuthToken())