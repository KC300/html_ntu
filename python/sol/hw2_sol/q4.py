ID = input()
num = 0
for i in range(8):
	num += int(ID[i]) * (8 - i)
num += int(ID[8])
remainder = (10 - num % 10) % 10
if (remainder == 0):
	print ("BNZ")
elif (remainder == 1):
	print ("AMW")
elif (remainder == 2):
	print ("KLY")
elif (remainder == 3):
	print ("JVX")
elif (remainder == 4):
	print ("HU")
elif (remainder == 5):
	print ("GT")
elif (remainder == 6):
	print ("FS")
elif (remainder == 7):
	print ("ER")
elif (remainder == 8):
	print ("DOQ")
elif (remainder == 9):
	print ("CIP")