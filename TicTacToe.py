import math
import sys
from termcolor import cprint, colored
import RandomAI as Randy


class Player():
	def __init__(self, name):
		self.name = name
		self.color = ''
		self.pieces = [1, 1, 2, 2, 3, 3]
		self.symbol = ''

	def valid_piece(self, piece):
		if (piece in self.pieces):
			return True
		return False

class Board():
	def __init__(self):
		self.state_pieces = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.state_player = [['', '', ''], ['', '', ''], ['', '', '']]

	def print_board(self):
		for row in range (0,3):
			for col in range (0,3):
				print(" | ", end = ' ')
				if (self.state_player[row][col] == 'X'):
					cprint(" %d " % (self.state_pieces[row][col]), 'magenta', end = ' ')
				elif (self.state_player[row][col] == '@'):
					cprint(" %d " % (self.state_pieces[row][col]), 'cyan', end = ' ')
				else:
					cprint(" %d " % (self.state_pieces[row][col]), end = ' ')

			print(" | ")
			print( " ------------------------- " )

	def valid_location(self, row, col, number):
		if (row in range(3) and col in range(3)):
			if (self.state_pieces[row][col] < number):
				return True
		return False

	def update_state(self, row, col, symbol, number):
			self.state_pieces[row][col] = number
			self.state_player[row][col] = symbol

def CheckWin(state):
	game_over = False

	#Checking lines
	for row in range (0,3):
		if ((state[row][0] == state[row][1]) and (state[row][0] == state[row][2])):
			if (state[row][0] != ''):
					game_over = True

	#Checking columns
	for col in range (0,3):
		if ((state[0][col] == state[1][col]) and (state[0][col] == state[2][col])):
			if (state[0][col] != ''):
				game_over = True

	#Checking diagonals
	if ((state[0][0] == state[1][1]) and (state[0][0] == state[2][2]) or 
		(state[2][0] == state[1][1]) and (state[2][0] == state[0][2])):
		if (state[1][1] != ''):
			game_over = True	
	return game_over

def main():
	#Welcomes
	cprint("Hello! You are about to play a different game from the old tic-tac-toe.", 'yellow')

	#Player 1 - X - magenta
	name1 = input("Player 1: ")
	player1 = Player(name1)
	player1.color = 'magenta'
	player1.symbol = 'X'

	#mode = input("Type 1 if you wish to play against someone, otherwise type 2 for an Easy AI or 3 for a Hard one")
	mode = 1
	#Player 2 - @ - cyan
	if (mode == 1):
		name2 = input("Player 2: ")
		player2 = Player(name2)
	else:
		player2 = Player("Randy")
	player2.color = 'cyan'
	player2.symbol = '@'

	board = Board()
	curPlayer = player1
	game_over = False

	#Game Loop
	while (not game_over):
		cprint("Pieces available for %s: " %player1.name)
		cprint(player1.pieces, player1.color)
		cprint("Pieces available for %s: " %player2.name)
		cprint(player2.pieces, player2.color)
		board.print_board()
		cprint("Turn: %s " %curPlayer.name, curPlayer.color)
		if (curPlayer == player1):
			row = int(input("Type the row you wish to place a piece: "))
			row-=1
			col = int(input("Type the col you wish to place a piece: "))
			col-=1
			piece = int(input("Type the piece you wish to play: "))
		else:
			if (mode == 1):
				row = int(input("Type the row you wish to place a piece: "))
				row-=1
				col = int(input("Type the col you wish to place a piece: "))
				col-=1
				piece = int(input("Type the piece you wish to play: "))
			else:
				row, col, piece = Randy.pick_random(board, player2)
		valid_move = board.valid_location(row, col, piece) and curPlayer.valid_piece(piece)
		if (valid_move):
			board.update_state(row, col, curPlayer.symbol, piece)
			game_over = CheckWin(board.state_player)
			curPlayer.pieces.remove(piece)
			if (curPlayer == player2):
				curPlayer = player1
			else:
				curPlayer = player2

		else:
			cprint ("Invalid play!", 'grey', 'on_red')
		print("------------------------------------")
		print()

	if (curPlayer == player2):
		curPlayer = player1
	else:
		curPlayer = player2

	board.print_board()
	cprint("WIN", curPlayer.color)

main()