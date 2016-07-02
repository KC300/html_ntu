n = int(input())
flag = 1
for i in range(2, n):
	if (i * i > n):
		break
	if (n % i == 0):
		flag = 0
		break
if (flag == 1):
	print ("Yes")
else:
	print ("No")