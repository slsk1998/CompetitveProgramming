from sys import stdin
input = stdin.readline
import math	
test = int(input())
for _ in range(test):
	n = int(input())
	l, r = 1 - n, n
	print(l, r)
