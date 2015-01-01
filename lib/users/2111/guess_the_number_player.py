import sys, random

def main():
	num_guesses = int(sys.argv[1])
	max_value = int(sys.argv[2])

	to_guess = max_value / 2
	increment = to_guess / 2

	while True:
		print(int(to_guess))
		sys.stdout.flush()
		
		response = input()
		if response == 'TOO_HIGH':
			to_guess -= increment
		else:
			to_guess += increment

		increment = max(1, increment // 2)


if __name__ == '__main__':
	main()