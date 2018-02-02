cont = 0

def fibo(n):
	global cont
	if(n == 1 or n == 0):
		return n
	else:
		cont += 2
		return fibo(n - 1) + fibo(n - 2)
		
times = input()

for i in range(times):
	n = input()
	fibon = fibo(n)
	print "fib(%d) = %d calls = %d" % (n,cont, fibon)
	cont = 0
