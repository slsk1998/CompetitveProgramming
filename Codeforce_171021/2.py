from sys import stdin
import math

input = stdin.readline
test = int(input())
for _ in range(test):
	n, k = map(int, input().split())
	done, cond = set(), {i : [] for i in range(1, n + 1)}
	for _ in range(k):
		a, b, c = map(int, input().split())
		done.add(b)
	root = None
	for i in range(1, n + 1):
		if(i not in done):
			root = i
			break
	for i in range(1, n + 1):
		if(i == root):continue
		print("%d %d"%(root, i))