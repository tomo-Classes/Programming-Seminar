def longestline(file):
	maxlenline = ""
	for line in file:
		if len(maxlenline) < len(line):
			maxlenline = line
	return maxlenline

if __name__ == "__main__":
	import sys
	sys.stdout.write(longestline(sys.stdin))
	# sys.stdout.write(longestline(open("./1-15_celsius-fahrenheit.py")))
