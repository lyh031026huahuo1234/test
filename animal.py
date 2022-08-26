import sys

def cat():
	print("cat")


def default():
	print("animal")

def main():
	if sys.argv[1] == 'cat' :
		cat()
	else:
		default()

if __name__ == '__main__':
	main()
