import sys, random

def main():
	num_guesses = int(sys.argv[1])
	max_value = int(sys.argv[2])

	while True:
		print(random.randint(0, max_value))
		sys.stdout.flush()
		input()

if __name__ == '__main__':
	main()