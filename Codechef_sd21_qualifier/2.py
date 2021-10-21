# test = int(input())
# for _ in range(test):
# 	arr = [0, 0, 0]
# 	for val in input().strip().split():
# 		arr[int(val)] += 1
# 	if(arr[1] == arr[2]):
# 		print("DRAW")
# 	elif(arr[1] > arr[2]):
# 		print("INDIA")
# 	else:
# 		print("ENGLAND")

def strRevRep(inpStr):
	if(len(inpStr) > 50):
		print("Invalid Input")
	else:
		vowels = set('aeiouAEIOU')
		newStr, count = "", 0
		nums = [i for i in range(1, 10)]
		for c in inpStr:
			if(c not in vowels):
				newStr += c
			else:
				newStr += str(nums[count % 9])
				count += 1
		print("".join(reversed(newStr)))
strRevRep('LanguageLanguageLanguage')