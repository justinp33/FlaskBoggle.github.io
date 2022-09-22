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