import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getByGenres_all(input_genres):
    # 設定Spotify API金鑰和密鑰
    client_id = 'client_id_here'
    client_secret = 'client_secret_here'

    # 創建授權流程
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # 定義要查詢的特定類型
    genres = input_genres
    print(genres)
    # 搜尋特定類型的歌曲
    genre_query = ' '.join([f'genre:"{genre}"' for genre in genres])
    results = sp.search(q=genre_query, type='track', limit=50)

    if results['tracks']['items']:
        # 從結果中隨機選擇一首歌曲
        random_track = random.choice(results['tracks']['items'])
        track_name = random_track['name']
        artist_name = random_track['artists'][0]['name']

        return f"{track_name} - {artist_name}"
    else:
        return f"找不到{', '.join(genres)}歌曲"
    #f"{', '.join(genres)}: