import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getByGenres_sep(input_genres):
    # 設定Spotify API金鑰和密鑰
    client_id = 'client_id_here'
    client_secret = 'client_secret_here'


    # 創建授權流程
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # 定義要查詢的特定類型
    genres = input_genres  # 更改為您想要的特定類型列表

    results_list = []

    for genre in genres:
        # 搜尋特定類型的歌曲
        results = sp.search(q=genre, type='track', limit=50)
        
        if results['tracks']['items']:
            # 從結果中隨機選擇一首歌曲
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
            print(f"找不到{genre}歌曲")
    return results_list
'''
    formatted_results = ''
    for track_info in results_list:
        genre = track_info['genre']
        track_name = track_info['track_name']
        artist_name = track_info['artist_name']
        formatted_results += f"Genre: {genre}<br>Track: {track_name}<br>Artist: {artist_name}<br><br>"

    return formatted_results'''
