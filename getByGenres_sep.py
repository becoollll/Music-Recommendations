import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getByGenres_sep(input_genres):
    # Set Spotify API key
    client_id = 'client_id_here'
    client_secret = 'client_secret_here'


    # Create authorization process
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Define the specific genre to search
    genres = input_genres  # Change to the desired list of specific genres

    results_list = []

    for genre in genres:
        # Search for songs of specific genres
        results = sp.search(q=genre, type='track', limit=50)
        
        if results['tracks']['items']:
            # Choose random songs from results
            random_track = random.choice(results['tracks']['items'])
            track_name = random_track['name']
            artist_name = random_track['artists'][0]['name']
            
            track_info = {
                'genre': genre,
                'track_name': track_name,
                'artist_name': artist_name
            }
            results_list.append(track_info)
        else:
            print(f"Cannot find {genre} songs")
    return results_list
'''
    formatted_results = ''
    for track_info in results_list:
        genre = track_info['genre']
        track_name = track_info['track_name']
        artist_name = track_info['artist_name']
        formatted_results += f"Genre: {genre}<br>Track: {track_name}<br>Artist: {artist_name}<br><br>"

    return formatted_results'''
