import math
from sys import stdin
input = stdin.readline

test = int(input())
for _ in range(test):
	n, arr, result = int(input()), [], True
	topic, diff, present = {}, {}, set()
	
	for _ in range(n):
		a, b = map(int, input().split()) # topic, difficulty
		topic[a] = topic.get(a, 0) + 1
		diff[b] = diff.get(a, 0) + 1

	
	for topic in topics:





