import math
from sys import stdin
input = stdin.readline

test = int(input())
for _ in range(test):
	n, arr, result = int(input()), [], True
	for _ in range(2):
		arr.append(input())
	for i in range(n):
		if(arr[0][i] == '1' and arr[1][i] == "1"):
			result = False
			break
	if(result):
		print("YES")
	else:
		print("NO")

