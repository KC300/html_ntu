def new_fibo(n):
	if (n == 1):
		return 1
	elif (n == 2):
		return 2
	elif (n == 3):
		return 3
	return new_fibo(n - 1) + new_fibo(n - 2) + new_fibo(n - 3)
n = int(input())
print (new_fibo(n))