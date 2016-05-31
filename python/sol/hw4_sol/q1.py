Input_num = input()
a = int(Input_num.split(",")[0])
b = int(Input_num.split(",")[1])
c = int(Input_num.split(",")[2])
if (a == 1):
	print (b + c)
elif (a == 2):
	print (b - c)
elif (a == 3):
	print (b * c)
elif (a == 4):
	print (b / c)
elif (a == 5):
	print (b % c)