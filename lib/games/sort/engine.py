# Guess a number up to max
import sys, random, json
from engine.game_board import GameBoard

class GameEngine(GameBoard):

	def __init__(self):
		super().__init__()

		self.file_requirements = ['sorting_game_player.py', 'sorting_game_driver.py'] 
		self.launch_string = "python3 sorting_game_driver.py"

	def play(self, manager):
		super().play(manager)

		full_report = ""

		while True:
			report = self.get_input()
			if report.find('DONE') != -1:
				break
			else:
				full_report += report

		self.signal_winner(full_report)
			
	# Get input from the client, and validate it
	def get_input(self):
		return super().get_input()

	def write_to_client(self, mesg):
		super().write_to_client(mesg)

