from sys import stdin
from collections import deque
input = stdin.readline
test = int(input())
for _ in range(test):
	_ = input()
	n, k = map(int, input().split())
	edges = {i : [] for i in range(1, n + 1)}
	degree = {i : 0 for i in range(1, n + 1)}
	queue = deque()
	for _ in range(n - 1):
		a, b = map(int, input().split())
		edges[a].append(b)
		edges[b].append(a)
		degree[a] += 1
		degree[b] += 1
	remove, total, step, current = set(), 0, 0, 0
	for i in range(1, n + 1):
		if(degree[i] <= 1):
			remove.add(i)
			degree.pop(i)
			current += 1
	k -= 1
	while(degree and step < k):
		newremove = set()
		for r in remove:
			# degree.pop(r)
			for edge in edges[r]:
				if(edge in degree and edge not in remove):
					degree[edge] -= 1
					if(degree[edge] <= 1):
						degree.pop(edge)
						newremove.add(edge)

		remove, step = newremove.copy(), step + 1
	print(len(degree))



