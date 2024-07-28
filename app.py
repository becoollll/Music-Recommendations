from flask import Flask, render_template, redirect, url_for,  request
from getGenres import getGenres
from getByGenres_all import getByGenres_all
from getByGenres_sep import getByGenres_sep
from knn_genre import knn_genre
from get_charts import get_charts
from markupsafe import Markup

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        flag = 0 ## whether the song exist or not.
        try:
            input_text = request.form['input_text']
            genres, artist_name, track_name = getGenres(input_text)
            SongsByG_all = Markup(getByGenres_all(genres))
            SongsByG_sep = getByGenres_sep(genres)
            genresByKNN = knn_genre(genres)
            SongsByKNN = getByGenres_sep(genresByKNN)
            
            flag = 0
            return render_template('index.html', flag = flag, input_text=input_text, genres=genres, artist_name=artist_name, track_name=track_name, SongsByG_all=SongsByG_all, SongsByG_sep=SongsByG_sep, genresByKNN=genresByKNN, SongsByKNN=SongsByKNN)
        except:
            flag = 1
            return render_template('index.html', flag = flag, input_text=input_text, genres='', artist_name='', track_name='', SongsByG_all='', SongsByG_sep='', genresByKNN='', SongsByKNN='')
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/charts')
def charts():
    songs = get_charts()
    return render_template('charts.html', songs=songs)

@app.route('/redirect')
def redirect_page():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
