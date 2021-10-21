from sys import stdin
input = stdin.readline
test = int(input())
for _ in range(test):
	n, k = map(int, input().split())
	arr, total, mod = [], 0, 1000000007
	while(k != 0):
		arr.append(k % 2)
		k = k // 2
	prev = 1
	for v in arr:
		total = (total + prev * v) % mod
		prev = (prev * n) % mod
	print(total)

