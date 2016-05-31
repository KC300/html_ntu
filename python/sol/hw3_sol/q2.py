def gcd(n1, n2):
	if (n1 % n2 == 0):
		return n2;
	return gcd(n2, n1 % n2)
s = input()
n1 = int(s.split(",")[0])
n2 = int(s.split(",")[1])
print (gcd(n1, n2))