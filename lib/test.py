import sys
import driver

from engine.one_player_game_manager import OnePlayerGameManager

def main():
	game_id = sys.argv[1]
	user_id = sys.argv[2]

	# unqualified directory name
	game_dir = driver.game_id_to_directory(game_id)
	_temp = __import__('games.{0}.engine'.format(game_dir), globals(), locals(), ['GameEngine'])
	
	GameEngine = _temp.GameEngine

	ge = GameEngine()
	manager = OnePlayerGameManager(ge, user_id, game_id)
	manager.run()
	
if __name__ == '__main__':
	main()