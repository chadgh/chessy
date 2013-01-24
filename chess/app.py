# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect
import urllib2
app = Flask('__name__')
app.debug = True

@app.route('/')
def home():
	mate_in_2 = [(p.strip(), m.strip()) for p, m in [line.split('|') for line in open('mate_in_2.fen')]]
	return render_template('index.html', puzzles=mate_in_2)

@app.route('/board/')
@app.route('/board/<path:fen>/message:<message>')
@app.route('/board/<path:fen>')
def display_chess_board(fen=None, message=None):
	from fenpy import fen as FEN
	fen = '' if fen == None else urllib2.unquote(fen.strip('/'))
	message = '' if message == None else urllib2.unquote(message)
	error = ''
	message = message if message is not None else ''
	try:
		game = FEN(fen)
	except:
		error = 'Not a valid FEN. ' + fen
		game = FEN()
	game.graphical_board = game._generate_graphical_board(True)
	return render_template('chessboard.html', game=game, error=error, message=message)

@app.route('/submit_fen/', methods=['POST'])
def rewrite_fen():
	return redirect(url_for('display_chess_board', fen=request.form['fen']))
