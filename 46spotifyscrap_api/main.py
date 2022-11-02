import requests
from bs4 import BeautifulSoup
import re
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = "2010-10-02/"
year = '2010'
URL = "https://www.billboard.com/charts/hot-100/"
date_URL = URL + date

response = requests.get(date_URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
songs = soup.find_all(name = "h3",  class_=re.compile('^c-title a-no-trucate*'))
song_list = [song.getText().strip() for song in songs] 
artists = soup.find_all(name="span", class_=re.compile('^c-label a-no-trucate*'))
artists_list = [artist.getText().strip() for artist in artists]


scope =  "playlist-modify-private" 
SPOTIFY_CLIENT_ID = config("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = config("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = config("SPOTIFY_REDIRECT_URI")
AUTH_URI = 'https://accounts.spotify.com/authorize'
TOKEN_URI = 'https://accounts.spotify.com/api/token'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=scope,
        show_dialog=True,
        cache_path="token.txt")
    )

user_id = sp.current_user()["id"]


uri_list = []
for song in song_list:
    try:
        uri_list.append(sp.search(q=f"track:{song} year:{year}", type="track")["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"Could not find {song} title")
    
    
date = "2010-10-02"
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", description="New playlist", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)