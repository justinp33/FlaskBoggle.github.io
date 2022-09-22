from boggle import Boggle
from flask import Flask, request, render_template, jsonify, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

boggle_game = Boggle()

@app.route('/')
def display_board():

    board = boggle_game.make_board()
    session['board'] = board

    return render_template("display.html", board=board)

@app.route("/check-word")
def check_word():
    """Check if word is in dictionary."""

    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)

    return jsonify({'result': response})