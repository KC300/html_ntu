total = int(input())
s = input()
num = s.split(",")
for i in range(len(num)):
	n = int(num[i])
	print (int(total / n), end = " ")
	total %= n
print ()