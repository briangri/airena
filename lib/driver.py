import os
import json
import shutil


def add_solution_by_file(user_id, game_id, solution_file, allow_dir=False):
	'''
	Store a solution file, given a specific user id and game id.

	Raises a StandardError if the user or game id is not recognized.
	'''
	# Back up the current working directory
	wd = os.getcwd()

	old_location = os.path.abspath(solution_file)

	# Make sure that we are in the lib directory
	os.chdir(os.path.dirname(__file__) or '.')

	# Make sure the game list is loaded
	load_registry()

	if not os.path.isdir('users/{0}'.format(user_id)):
		os.path.chdir(wd)
		raise StandardError('User {0} is unknown'.format(user_id))

	if not allow_dir and os.path.isdir(old_location):
		os.path.chdir(wd)
		raise StandardError('Submission is directory!')

	new_solution_name = game_id_to_filename(game_id)
	shutil.copyfile(old_location, 'users/{0}/{1}'.format(user_id, new_solution_name))

	# Restore former working directory
	os.chdir(wd)

def get_solution_file(user_id, game_id):
	'''
	Return the location of a previously registered solution for a given user
	and game.

	Throws a standard error if user is not found; returns None if the user has
	no submissions for this game
	'''
	# Back up the current working directory
	wd = os.getcwd()

	# Make sure that we are in the lib directory
	os.chdir(os.path.dirname(__file__) or '.')

	if not os.path.isdir('users/{0}'.format(user_id)):
		os.path.chdir(wd)
		raise StandardError('User {0} is unknown'.format(user_id))

	solution_name = game_id_to_filename(game_id)
	solution_file = os.path.join(os.getcwd(), 'users/{0}/{1}'.format(user_id, solution_name))
	
	if not os.path.exists(solution_file):
		return None

	# Restore former working directory
	os.chdir(wd)
	return solution_file

def get_user_directory(user_id):
	'''
	Returns the directory containing the user's submissions
	'''
	wd = os.getcwd()
	os.chdir(os.path.dirname(__file__) or '.')

	if not os.path.isdir('users/{0}'.format(user_id)):
		os.path.chdir(wd)
		raise StandardError('User {0} is unknown'.format(user_id))

	os.chdir('users/{0}'.format(user_id))
	p = os.getcwd()

	# Restore former working directory
	os.chdir(wd)
	return p

def get_game_directory(game_id):
	'''
	Returns the directory containing the game's files
	'''
	wd = os.getcwd()
	os.chdir(os.path.dirname(__file__) or '.')

	d = game_id_to_directory(game_id)

	if not os.path.isdir('games/{0}'.format(d)):
		os.path.chdir(wd)
		raise StandardError('Could not find game directory is unknown')

	os.chdir('games/{0}'.format(d))
	p = os.getcwd()

	# Restore former working directory
	os.chdir(wd)
	return p


def game_id_to_filename(game_id):
	'''
	Returns the name of the player.py file for a given game game_id

	Raises a StandardException if the game_id is not found
	'''
	return _game_id_to_info(game_id, 'player_filename')

def game_id_to_directory(game_id):
	'''
	Returns the name of the directory in lib/games that holds files for the
	given game_id

	Raises a StandardException if the game_id is not found
	'''
	return _game_id_to_info(game_id, 'directory')

def game_id_to_numplayers(game_id):
	'''
	Returns the number of players for a given game id

	Raises a StandardException if the game_id is not found
	'''
	return _game_id_to_info(game_id, 'num_players')

def _game_id_to_info(game_id, field):
	registry = json.load(open('games/game_list.json', 'r'))
	if game_id not in registry:
		raise StandardError('Game id {0} not found!'.format(game_id))
	return registry[str(game_id)][field]	

def load_registry():
	'''
	Load the game list into the global 'registry' variable. If it has 
	already been loaded, this does nothing
	'''



