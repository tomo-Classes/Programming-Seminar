def match(target, str):
	ret = -1
	for i, char in enumerate(target):
		# print(char, i)
		if ret == -1 and char == str[0]:
			ret = i
		elif ret > -1:
			if i - ret == len(str):
				break
			if char != str[i - ret]:
				ret = -1
	return ret

if __name__ == "__main__":
	print(match(input(), input()))
