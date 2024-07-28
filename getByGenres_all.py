import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getByGenres_all(input_genres):
    # Set Spotify API key
    client_id = 'client_id_here'
    client_secret = 'client_secret_here'


    # Create authorization process
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Define the specific genre to search
    genres = input_genres
    print(genres)
    # Search for songs of specific genres
    genre_query = ' '.join([f'genre:"{genre}"' for genre in genres])
    results = sp.search(q=genre_query, type='track', limit=50)

    if results['tracks']['items']:
        # Choose random songs from results
        random_track = random.choice(results['tracks']['items'])
        track_name = random_track['name']
        artist_name = random_track['artists'][0]['name']

        return f"{track_name} - {artist_name}"
    else:
        return f"Cannot find {', '.join(genres)} songs"
    #f"{', '.join(genres)}: