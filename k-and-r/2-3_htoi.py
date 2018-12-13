def htoi(str):
	if str[0:2].lower() == "0x":
		str = str[2:]
	ret = 0
	dig = len(str)
	for c in str:
		dig -= 1
		add = 0
		if 48 <= ord(c) and ord(c) <= 57:
			add = (ord(c) - 48)
		elif 65 <= ord(c) and ord(c) <= 70:
			add = (ord(c) - 55)
		elif 97 <= ord(c) and ord(c) <= 102:
			add = (ord(c) - 87)
		else:
			raise ValueError("!")
		ret += add * (16 ** dig)
	return ret

if __name__ == "__main__":
	print(htoi(input()))
