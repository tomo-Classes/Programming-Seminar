MAXLEN = 255

def compress(infile, outfile):
	target = infile.read(MAXLEN)
	print("\n")
	while target:
		print("len(target) =" + str(len(target)))
		print("==target==\n" + target)
		compressing = 0
		prev = ""
		for i in range(len(target)):
			if compressing and prev != target[i]:
				outfile.write(str_repeated(prev, i))
				break
			elif not compressing and prev == target[i]:
				if i == 1:
					compressing = 1
				elif i > 1:
					outfile.write(str_through(target[:i]))
					break
			prev = target[i]
			print("i =", i, "/ ord(target[i])", ord(prev))
		else:
			if compressing:
				outfile.write(str_repeated(prev, len(target)))
			else:
				outfile.write(str_through(target))
			target = infile.read(MAXLEN)
			print("\n==continue==\n" + target)
			continue
		print("i =", i)
		if i < len(target):
			print("i < len(target): i =", i)
			print("==target[i:]==\n" + target[i:])
			target = target[i:] + infile.read(i)
			print("==target[i:] + infile.read(i)==\n" + target)

def str_repeated(char, cnt):
	return bytes([0, ord(char), cnt])

def str_through(text):
	return bytes([len(text)]) + text.encode()

if __name__ == "__main__":
	import sys
	# compress(sys.stdin, sys.stdout.buffer)
	compress(sys.stdin, open("./compress.out", "wb"))

	# target = sys.stdin.read(4)
	# print("\n")
	# while target:
	# 	print(target)
	# 	target = sys.stdin.read(4)
