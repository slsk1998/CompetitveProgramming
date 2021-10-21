from sys import stdin
input = stdin.readline
test = int(input())
possible = ['00', '25', '50', "75"]
for _ in range(test):
	d1 = {'0' : [], '7' : [], '5' : [], '2' : []}
	d2 = {'0' : 0, '7' : 0, '5' : 0, '2' : 0}
	n = input().strip()
	length = len(n)
	# print(length)
	for i in range(length):
		if(n[i] in d2):
			d1[n[i]].append(i)
			d2[n[i]] += 1
	result = length
	# print(d1, d2)
	for word in possible:
		a, b = word[0], word[1]
		if(d2[a] and d2[b]):
			for i in d1[a]:
				for j in d1[b]:
					if(i < j):
						# print(a+b, length, i, j, n)
						result = min(result, length - 1 - j + j - i - 1)
	print(result)

