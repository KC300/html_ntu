def guess_num(guess, ans):
	A = 0
	B = 0
	for i in range(4):
		for j in range(4):
			if (guess[i] == ans[j]):
				if (i == j):
					A = A + 1
				else:
					B = B + 1
	return str(A) + "A" + str(B) + "B" 
Input_num = input()
ans = (Input_num.split(",")[0])
m = int(Input_num.split(",")[1])
for i in range(m):
	guess = input()
	result = guess_num(guess, ans)
	print (result)