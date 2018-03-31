from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from modules import character_data

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SECRET_KEY'] = 'BgzNrDP34D'

Bootstrap(app)

def get_char(source, id):
    for row in source:
        if id == str( row["id"] ):
            character = row["character"]
            actor = row["actor"]
            movie = row["movie"]
            year_released = row["year released"]
            movie_imdb_url = row["movie imdb url"]
            id = str(id)
            return id, character, actor, movie, year_released, movie_imdb_url

@app.route('/')
def index():
    ids_list = []
    name_list = []
    for character in character_data:
        ids_list.append(character['id'])
        name_list.append(character['character'])
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title=("Wes Anderson Characters"))

@app.route('/character/<id>.html')
def character(id):
    id, character, actor, movie, year_released, movie_imdb_url = get_char(character_data, id)
    return render_template('character.html', character=character, actor=actor, movie=movie, year_released=year_released, movie_imdb_url=movie_imdb_url)

if __name__ == '__main__':
    app.run(debug=True)
