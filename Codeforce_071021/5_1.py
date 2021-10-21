k = int(input())
val, prev, mod = 6, 16, 1000000007
for i in range(1, k):
	val = (val * prev) % mod
	prev = (prev * prev) % mod
print(val)