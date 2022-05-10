from flask import Flask, render_template
from random import randint
import game_of_life as gom

app = Flask(__name__)


@app.route('/')
def index():
    gom.GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    game = gom.GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
