from sys import stdin
input = stdin.readline
test = int(input())
for _ in range(test):
	n, k = map(int, input().strip().split(" "))
	arr = list(map(int, input().split()))
	arr.sort()
	start, result, idx = 0, 0, k - 1
	while(idx > -1 and start  < arr[idx]):
		result += 1
		start += n - arr[idx]  
		idx -= 1
	print(result)
