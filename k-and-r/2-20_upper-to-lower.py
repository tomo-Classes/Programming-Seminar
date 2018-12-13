def lower(str):
	ret = ""
	for i, c in enumerate(str):
		# print(c)
		if ord(c) >= 65 and ord(c) <= 91:
			ret += chr(97 + ord(c) - 65)
		else:
			ret += c
	return ret

	# for i, c in enumerate(str):
	# 	if ord(c) >= 65 and ord(c) <= 91:
	# 		str[i] = chr(97 + ord(c) - 65)
	# 	else:
	# 		str[i] = c
	# return str

if __name__ == "__main__":
	import sys
	print(lower(sys.stdin.read()))
