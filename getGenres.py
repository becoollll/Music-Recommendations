import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getGenres(input_text):

    client_id = 'client_id_here'
    client_secret = 'client_secret_here'


    # Create the authorization flow
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for a specific song
    song_name = input_text
    results = sp.search(q=f"track:{song_name}", type='track', limit=1)

    # Retrieve the song's genre, artist, and track name
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_id = track['id']

        track_info = sp.track(track_id)
        artist_id = track_info['artists'][0]['id']
        artist_info = sp.artist(artist_id)
        genres = artist_info['genres']
        artist_name = artist_info['name']
        track_name = track_info['name']
        return genres, artist_name, track_name
    else:
        return f"找不到歌曲 '{song_name}'"

