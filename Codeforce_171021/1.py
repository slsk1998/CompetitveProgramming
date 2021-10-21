from sys import stdin
import math

def iscomposite(summ):
	for i in range(2, int(math.sqrt(summ)) + 1):
		if(summ % i == 0):
			return True
	return False

input = stdin.readline
test = int(input())
for _ in range(test):
	n = int(input())
	arr = list(map(int, input().split()))
	summ = sum(arr)
	if(summ % 2 == 0 or iscomposite(summ)):
		print(n)
		print(" ".join(map(str, range(1, n + 1))))
	else:
		check, net = 1, []
		for i in range(n - 1, -1, -1):
			if(arr[i] % 2 == check):
				check = 1000
			else:
				net.append(i + 1)
		print(n - 1)
		print(" ".join(map(str, net)))
