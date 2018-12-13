def rpn(str):
	arr = str.split(" ")
	stack = []
	for v in arr:
		try:
			stack.append(int(v))
		except ValueError:
			if v == "+":
				return stack[0] + stack[1]
			elif v == "-":
				return stack[0] - stack[1]
			elif v == "*":
				return stack[0] * stack[1]
			elif v == "/":
				return stack[0] / stack[1]
			else:
				print("operator exception")
			stack = []

print(rpn("10 2 +"))
print(rpn("10 2 -"))
print(rpn("10 2 *"))
print(rpn("10 2 /"))
