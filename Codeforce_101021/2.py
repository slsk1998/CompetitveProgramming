import math
from sys import stdin
input = stdin.readline

test = int(input())
for _ in range(test):
	n, arr, result = int(input()), [], True
	arr = [set() for _ in range(5)]
	for j in range(n):
		data = list(map(int, input().split()))
		for i in range(5):
			if(data[i]):
				arr[i].add(j)
	if(n % 2 == 1):
		print("NO")
		continue
	result = False
	for i in range(5):
		a = len(arr[i])
		if(a < n//2 or result):continue
		for j in range(i + 1, 5):
			b = len(arr[j])
			if(b < n//2):continue
			union = len(arr[i].union(arr[j]))
			if(union == n):
				result = True
	if(result):
		print("YES")
	else:
		print("NO")

