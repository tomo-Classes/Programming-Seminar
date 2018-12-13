def escape(str):
	ret = ""
	for char in str:
		if char == "\n":
			ret += "\\n"
		elif char == "\t":
			ret += "\\t"
		else:
			ret += char
	return ret

def unescape(str):
	ret = ""
	flag = False
	for i, char in enumerate(str):
		if char == "\\":
			flag = True
		elif flag and char == "n":
			ret += "\n"
			flag = False
		elif flag and char == "t":
			ret += "\t"
			flag = False
		elif flag:
			ret += "\\" + char
			flag = False
		else:
			ret += char
	return ret

if __name__ == "__main__":
	import sys
	print(escape(sys.stdin.read()))
	print(unescape(input()))
