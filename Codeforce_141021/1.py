test = int(input())
for _ in range(test):
	a, b, c = map(int, input().strip().split(" "))
	print(max(0, 1 + max(b, c) - a), max(0, 1 + max(a, c) - b), max(0, 1 + max(b, a) - c))