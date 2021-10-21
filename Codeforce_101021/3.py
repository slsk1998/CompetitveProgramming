import math
from sys import stdin
input = stdin.readline

test = int(input())
for _ in range(test):
	n, arr, result = int(input()), [], True
	arr = list(map(int, input().split()))
	k = (sum(arr)*1.0)/len(arr)
	d, res = {}, 0
	for a in arr:
		if(2*k - a in d):
			res += d[2*k - a]
		d[a] = d.get(a, 0) + 1
	print(res)