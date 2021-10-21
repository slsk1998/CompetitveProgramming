from sys import stdin
input = stdin.readline
test = int(input())
for _ in range(test):
	n, l = input().strip().split()
	word, n, count = input().strip(), int(n), 0
	maxi, length = -1, len(word)
	for i, c in enumerate(word):
		if(c != l):
			count += 1
		else:
			maxi = max(maxi, i + 1)
	if(count == 0):
		print(0)
	elif(maxi > n//2):
		print("1\n%d"%(maxi))
	else:
		print("2\n%d %d"%(n - 1, n))
