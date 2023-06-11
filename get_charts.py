from bs4 import BeautifulSoup
import requests

def get_charts():
    headers={
        "Referer": "https://open.spotify.com/",
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    response = requests.get('https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF', headers = headers)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup.prettify())
    meta_tag = soup.find_all('meta', attrs={'name': 'music:song'})
    urls = []
    for tag in meta_tag:
        urls.append(tag['content'])

    songs = []

    count = 1
    for url in urls:
        res = requests.get(url, headers = headers)
        ret = res.content

        soup = BeautifulSoup(ret, 'html.parser')
        temp = soup.find("title")
        song = temp.text.split(" | ")[0].split(" - song and lyrics by ")[0]
        artist = temp.text.split(" | ")[0].split(" - song and lyrics by ")[1]
        temp = {
            'ranking': count,
            'song': song,
            'artist': artist,
            'link': url
        }
        songs.append(temp)
        count += 1

    return songs