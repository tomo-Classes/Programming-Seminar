def rpn(str):
	arr = str.split(" ")
	stack = []
	for v in arr:
		try:
			stack.append(int(v))
		except:
			if v == "+":
				stack.append(stack.pop(-2) + stack.pop(-1))
			elif v == "-":
				stack.append(stack.pop(-2) - stack.pop(-1))
			elif v == "*":
				stack.append(stack.pop(-2) * stack.pop(-1))
			elif v == "/":
				stack.append(stack.pop(-2) / stack.pop(-1))
			else:
				raise("operator exception")
	return stack[0]

if __name__ == "__main__":
	# print(rpn("10 2 +"))
	# print(rpn("10 2 -"))
	# print(rpn("10 2 *"))
	# print(rpn("10 2 /"))

	# print(rpn("10 6 * 3 / 5 + 1 -")) # 10 * 6 / 3 + 5 - 1 = 24
	print(rpn(input()))
