from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

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

song_title = 'Black And Yellow'

# headers = {
#     "Authorization": AUTH_URI,
#     "Content-Type": "application/json"
# }

# spotify_params = {
#     "q": (f"track: {song_title} year:2010"),
#     "type": "track",
# }

# SPOTIFY_ENDPOINT = 'https://api.spotify.com/v1/search'

# response = requests.get(SPOTIFY_ENDPOINT, params=spotify_params, headers=headers)
# print(response.text)

result = sp.search(q=f"track:{song_title} year:{2010}", type="track")["tracks"]["items"][0]["uri"]
print(result)
date = "2010-10-02"
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", description="New playlist", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=result)
