def lineover80chars(file):
	ret = ""
	for line in file:
		count = 0
		for char in line:
			if char != "\n":
				count += 1
		if count > 80:
			ret += line
	return ret

if __name__ == "__main__":
	import sys
	sys.stdout.write(lineover80chars(sys.stdin))
	# sys.stdout.write(lineover80chars(open("./1-15_celsius-fahrenheit.py")))
