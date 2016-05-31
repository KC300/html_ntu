n = int(input())
ans = [[0 for i in range(n)] for j in range(n)]
num = 1
for i in range(int((n + 1) / 2)):
	for j in  range(i, n - i):
		ans[i][j] = num
		num = num + 1
	for j in range(i + 1, n - i):
		ans[j][n - i - 1] = num
		num = num + 1
	for j in range(i + 1, n - i):
		ans[n - i - 1][n - j - 1] = num
		num = num + 1
	for j in range(i + 1, n - i - 1):
		ans[n - j - 1][i] = num
		num = num + 1
for i in ans:
	for j in i:
		print (j, end = "	")
	print ()