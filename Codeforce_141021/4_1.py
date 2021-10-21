from sys import stdin
input = stdin.readline
test = int(input())
def gcd(a, b):
	if(a % b == 0):
		return b
	return gcd(b, a % b)
for _ in range(test):
	n = int(input())
	arr = list(map(int, input().split()))
	val, i, g = min(arr), 0, 0
	while(i < n and arr[i] == val):
		i += 1
	if(i == n):
		print(-1)
	else:
		g = arr[i] - val
		for j in range(i + 1, n):
			if(arr[j] != val):
				g = gcd(arr[j] - val, g)
		print(g)

