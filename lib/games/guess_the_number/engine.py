# Guess a number up to max
import sys, random, json
from engine.game_board import GameBoard

OVERALL_MAX = 1000
GUESSES = 10

class GameEngine(GameBoard):

	def __init__(self):
		super().__init__()
		self.max_val = random.randint(0, OVERALL_MAX)
		self.correct_num = random.randint(0, self.max_val)
		self.num_guesses = 0

		# Launch info
		# What files are required? The user's solution is required by default
		# We first look in the same directory as the engine, then in the user's
		# directory
		self.file_requirements = ['guess_the_number_player.py'] 

		# Command to launch?
		self.launch_string = "python3 guess_the_number_player.py {0} {1}".format(self.num_guesses, self.max_val)

	def play(self, manager):
		super().play(manager)

		while self.num_guesses < GUESSES:
			guess = self.get_input()
			self.num_guesses += 1
			if guess == self.correct_num:
				self.done(victory=True)
				return
			elif guess > self.correct_num:
				self.write_to_client('TOO_HIGH')
			else:
				self.write_to_client('TOO_LOW')

		self.done(victory=False)

	# Get input from the client, and validate it
	def get_input(self):
		message = super().get_input()
		try:
			x = int(message)
		except ValueError:
			raise ValueError('Invalid Input (not an int)')
		if x > OVERALL_MAX or x < 0:
			raise ValueError('Invalid input (outside of range)')
		return x

	def write_to_client(self, mesg):
		super().write_to_client(mesg)

	def done(self, victory=False):
		log = json.dumps({
			"answer": self.correct_num,
			"max_num": self.max_val,
			"guesses": self.num_guesses
		})
		if victory:
			self.signal_winner(log)
		else:
			self.signal_loss(log)
