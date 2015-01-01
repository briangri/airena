import random
import sorting_game_player
import timeit

def test():
	t = timeit.Timer("""
		s = sorting_game_player.sort(arr)
		""", """
import sorting_game_player
import random

arr = []
for _ in range(100):
	arr.append(random.randint(0, 50000))
		""")
	print(t.timeit(number=1000))
	print("DONE")

test()