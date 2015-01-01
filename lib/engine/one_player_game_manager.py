import subprocess
import logging
import time
import shutil
import os

import driver

logging.basicConfig(level=logging.DEBUG,
	format="[%(name)s] %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

class OnePlayerGameManager:

	def __init__(self, game_board, user_id, game_id):
		self.game_board = game_board
		self.user_id = user_id
		self.game_id = game_id

	def run(self):
		self.start_client()
		self.game_board.play(self)

	# TODO: sandbox
	def start_client(self):

		# Gather all of the needed files
		file_locations = []
		for filename in self.game_board.file_requirements:
			user_directory = driver.get_user_directory(self.user_id)
			game_dir = driver.get_game_directory(self.game_id)

			if os.path.exists(os.path.join(game_dir, filename)):
				file_locations.append(os.path.join(game_dir, filename))
			elif os.path.exists(os.path.join(user_directory, filename)):
				file_locations.append(os.path.join(user_directory, filename))
			else:
				raise StandardError('Could not find required file {0}'.format(filename))

		# Create a temporary file for them to live
		self.temp_dir = 'tmp_{0}_{1}_{2}'.format(self.user_id, self.game_id, time.time())
		os.mkdir(self.temp_dir)

		for f in file_locations:
			shutil.copy(f, os.path.join(self.temp_dir))

		# And finally, run the requested command
		self.original_wd = os.getcwd()
		os.chdir(self.temp_dir)

		logger.info("Starting process: " + self.game_board.launch_string)

		self.client_proc = subprocess.Popen(
			self.game_board.launch_string.split(' '),
			stdout=subprocess.PIPE,
			stdin=subprocess.PIPE
		)


	def write_to_client(self, mesg):
		logging.debug('Writing to client: ' + mesg)
		self.client_proc.stdin.write(bytes(mesg + "\n", 'UTF-8'))
		self.client_proc.stdin.flush()

	def read_line_from_client(self):
		temp = self.client_proc.stdout.read().rstrip().decode('UTF-8')
		logging.debug('Read from client: ' + temp)
		return temp

	def end_game(self):
		self.client_proc.kill()
		os.chdir(self.original_wd)
		shutil.rmtree(self.temp_dir)
