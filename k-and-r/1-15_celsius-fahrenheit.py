def convert_ftoc(deg):
	return (deg - 32) * 5 / 9

if __name__ == "__main__":
	import sys
	sys.stdout.write(str(convert_ftoc(int(sys.stdin.readline()))))
