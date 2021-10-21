from sys import stdin
import math

input = stdin.readline
n, m = map(int, input().split())
inputs = []
for _ in range(n):
	inputs.append(input().strip())
dp = [[-1]*m for _ in range(n)] # Stores maximum value of column that is causing the issue
# Doubt arises when we say not exitable because it can be X or . covered so it cant exit
for i in range(m):
	dp[0][i] = i if inputs[0][i] == 'X' else -1
for i in range(n):
	dp[i][0] = 0 if inputs[i][0] == 'X' else -1

arr = [-1] * m
for i in range(1, n):
	for j in range(1, m):
		dp[i][j] = min(dp[i-1][j], dp[i][j-1])
		if(dp[i][j] != -1):
			arr[j] = max(arr[j], dp[i][j])
		if(inputs[i][j] == 'X'):
			dp[i][j] = j


for i in range(1, m):
	arr[i] = max(arr[i], arr[i - 1])


for _ in range(int(input())):
	c1, c2 = map(int, input().split())
	if(arr[c2 - 1] < c1 - 1):
		print("YES")
	else:
		print("NO")