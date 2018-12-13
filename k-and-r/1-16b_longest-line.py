def longestline(file):
	maxlen = ["", 0]
	for line in file:
		count = 0
		for char in line:
			count += 1
		if maxlen[1] < count:
			maxlen[0] = line
			maxlen[1] = count
	return maxlen[0]

if __name__ == "__main__":
	import sys
	sys.stdout.write(longestline(sys.stdin))
	# sys.stdout.write(longestline(open("./1-15_celsius-fahrenheit.py")))
