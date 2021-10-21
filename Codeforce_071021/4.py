from sys import stdin
input = stdin.readline
import math	
test = int(input())
for _ in range(test):
	n, m = map(int, input().split())
	# edges = {str(i) : {"imposter":[], "crewmate":[]} for i in range(1, 1 + n)}
	first, second = set(), set()
	for _ in range(m):
		i, j, c = input().split()
		f1, f2, s1, s2, res = i in first, j in first, i in second, j in second, -1
		if(c[0] == 'i'): # Both people should be differnt
			if((f1 and f2) or (s1 and s2)):
				print(-1);continue
			if(f1 and not s2):
				second.add(j)
			elif(s1 and not f2):
				first.add(j)
			elif(f2 and not s1):
				second.add(i)
			elif(s2 and not f1):
				first.add(i)
			elif(not (f1 or s1) and not (f2 or s2)):
				first.add(i); second.add(j)


		else:# Both in same teams
			if((f1 and s2) or (f2 and s1)):
				print(-1); continue
			if(f1 and not f2):
				first.add(j)
			elif(s1 and not s2):
				second.add(j)
			elif(f2 and not f1):
				first.add(i)
			elif(s2 and not s1):
				second.add(i)
			elif(len(first) > len(second)):
				first.add(i); first.add(j)
			else:
				second.add(i); second.add(j)


		print(i, j, c, first, second)	
