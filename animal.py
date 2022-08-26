import sys

def dog():
	print("dog!")

def default():
	print("animal")

def main():
	if sys.argv[1] == 'dog':
		dog()
	else:
		default()

if __name__ == '__main__':
	main()
