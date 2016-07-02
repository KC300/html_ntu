Input_num = input()
a0 = int(Input_num.split(",")[0])
r = int(Input_num.split(",")[1])
n = int(Input_num.split(",")[2])
ans = a0
for i in range(n - 1):
	ans = ans * r
print (ans)