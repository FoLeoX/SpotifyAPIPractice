import requests
import json
import sys
from urllib.parse import urlencode

def getAuthToken():
    headers = {'Authorization': 'Basic MWUzMTIzMmMzMjMwNDIzZGI3M2FkYTE2MWE....I0MThkNThkY2RkZWJmMTQ4ZTU=',}
    data = {'grant_type': 'client_credentials'}
    r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    if r.status_code == 200:
        return r.json()["access_token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def getArtist(str_artist):
    headers = {"Authorization": f"Bearer {getAuthToken()}"}
    data = urlencode({"q": str_artist, "type": "artist"})
    endpoint = 'https://api.spotify.com/v1/search'
    lookup_url = f"{endpoint}?{data}"
    r = requests.get(lookup_url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        Genres_TYPES = data['artists']['items'][0]['genres']
        Artist_NAME = data['artists']['items'][0]['name']
        Artist_URI = data['artists']['items'][0]['id']
        print(Artist_NAME, "Found - Here You Go!")
        n = 1
        for genre in Genres_TYPES:
            print("{"+ str(n) +"}",genre)
            n +=1
    else:
        print(str_artist, "Not Found")
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to fetch Data.")
    return Artist_NAME, Artist_URI

while True:
    artist = input("Which Artist would you like to lookup: ")  
    print("============================================================================================================")
    getArtist(artist)
    response = input("Would you like a link to search a new artist ? (yes/no)")
    if response == "yes":
        True
    else:
        sys.exit()