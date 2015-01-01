import logging

logging.basicConfig(level=logging.DEBUG,
	format="[%(name)s] %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

class GameBoard:
	def __init__(self):
		pass

	def signal_winner(self, logging_info=""):
		logger.info("Logged win! " + logging_info)
		self.manager.end_game()

	def signal_loss(self, logging_info=""):
		logger.info("Logged loss! " + logging_info)
		self.manager.end_game()

	def play(self, manager):
		self.manager = manager

	def get_input(self):
		return self.manager.read_line_from_client()

	def write_to_client(self, mesg):
		self.manager.write_to_client(mesg)
