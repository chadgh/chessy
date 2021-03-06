# -*- coding: utf-8 -*-
class fen(object):
	"""Represents a FEN and provides parsing functionality."""
	def __init__(self, fen_str=None):
		super(fen, self).__init__()
		self.fen_str = fen_str
		self.fen_board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
		self.active_color = 'w'
		self.fen_castling = 'KQkq'
		self.en_passant = '-'
		self.halfmove_clock = 0
		self.fullmove_number = 1

		if fen_str is not None:
			self.fen_board, self.active_color, self.fen_castling, self.en_passant, self.halfmove_clock, self.fullmove_number = fen_parse(fen_str)
		else:
			self.fen_str = " ".join([self.fen_board, self.active_color, self.fen_castling, self.en_passant, str(self.halfmove_clock), str(self.fullmove_number)])

		self.board = self._generate_board()
		self.graphical_board = self._generate_graphical_board()
		self.turn = 'White' if self.active_color == 'w' else 'Black'

	def display_board(self, row_del="\n", cell_del=' ', with_rank=False, graphical=False):
		"""Print the board in a user friendly way."""
		board = self.graphical_board if graphical else self.board
		rows = [cell_del.join(cells) for cells in board]
		if with_rank:
			rank = 1
			for row in rows:
				row = str(rank) + cell_del + row
				rank += 1
		return row_del.join(rows)

	def _generate_board(self):
		rows = self.fen_board.split('/')
		board = []
		for row in rows:
			cells = list(row)
			row = []
			for cnum, cell in enumerate(cells):
				if cell.isdigit():
					row.extend(' '*int(cell))
				else:
					row.append(cell)
			board.append(row)

		return board

	def _generate_graphical_board(self, status=False):
		graphical_board = []
		for row in self.board:
			new_row = []
			for cell in row:
				new_row.append(self._get_graphical_piece(cell, status))
			graphical_board.append(new_row)

		return graphical_board
		
	def __repr__(self):
		return "%s('%s')" % ('fen', self.fen_str)

	def __str__(self):
		return self.fen_str

	def _get_graphical_piece(self, piece, status=False):
		LETTER_PIECES = ['K', 'Q', 'B', 'N', 'R', 'P', 'k', 'q', 'b', 'n', 'r', 'p', ' ']
		GRAPHICAL_PIECES = [u'♔', u'♕', u'♗', u'♘', u'♖', u'♙', u'♚', u'♛', u'♝', u'♞', u'♜', u'♟', ' ']
		rtn = GRAPHICAL_PIECES[LETTER_PIECES.index(piece)]
		if status:
			rtn = (GRAPHICAL_PIECES[LETTER_PIECES.index(piece.lower())], 'w' if piece in LETTER_PIECES[:6] else 'b')
		return rtn


def fen_parse(fen):
	fen_board, active_color, fen_castling, en_passant, halfmove_clock, fullmove_number = fen.split(' ')
	halfmove_clock = int(halfmove_clock)
	fullmove_number = int(fullmove_number)
	return (fen_board, active_color, fen_castling, en_passant, halfmove_clock, fullmove_number)

if __name__ == '__main__':
	import sys
	game = fen(" ".join(sys.argv[1:]))
	print game.display_board(graphical=True)
