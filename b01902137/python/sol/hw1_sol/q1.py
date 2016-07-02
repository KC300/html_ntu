ID = input()
num = 0
num += int(ID[0]) * 8
num += int(ID[1]) * 7
num += int(ID[2]) * 6
num += int(ID[3]) * 5
num += int(ID[4]) * 4
num += int(ID[5]) * 3
num += int(ID[6]) * 2
num += int(ID[7])
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