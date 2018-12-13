from functools import reduce

def average(arr):
	return reduce(lambda p, c: p + c, arr) / len(arr)

def variance(arr):
	ave = average(arr)
	arr = list(map(lambda x: (x - ave) ** 2, arr))
	return average(arr)

if __name__ == "__main__":
	import sys
	print("input comma separated list")
	a = list(map(int, sys.stdin.readline().split(",")))
	print("average:", average(a))
	print("variance:", variance(a))
