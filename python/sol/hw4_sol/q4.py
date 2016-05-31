Input_num = input()
n = int(Input_num.split(",")[0])
m = int(Input_num.split(",")[1])
total = 0
count = 0
while (total <= m):
	total = total + n
	n = n + 1
	count = count + 1
print (count)