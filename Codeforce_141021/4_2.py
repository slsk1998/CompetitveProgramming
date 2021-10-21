from sys import stdin
from bisect import bisect_right
input = stdin.readline
test = int(input())
def gcd(a, b):
	if(a % b == 0):
		return b
	return gcd(b, a % b)
for _ in range(test):
	n = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	if(arr[n // 2 - 1] == arr[0]):
		print(-1); continue
	val, i, g = arr[0], 0, 0
	i = bisect_right(arr, val)
	need_to_set = n // 2 - i
