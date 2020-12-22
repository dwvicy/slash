from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



date = input('What is your special date? Enter in the form of YYYY-MM-DD: ')





response = requests.get('https://www.billboard.com/charts/hot-100/' + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_all = soup.find_all('span', class_='chart-element__information__song')

song_name = [song.getText() for song in song_all]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= "CLIENT TOKEN",
        client_secret= "CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

print(user_id)

song_uris = []
year = date.split("-")[0]
day = date.split("-")[2]
month = date.split("-")[1]
for song in song_name:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist.")
        



playlist = sp.user_playlist_create(user=user_id, name=f"Era of {day}/{month}/{year}", public=False)
print(playlist)

playlist = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)