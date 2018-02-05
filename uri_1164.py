def check_divisor(n):
	divisor = [1]
	for i in range(2, (n/2)+1):
		if(n % i == 0):
			divisor.append(i)
	return sum(divisor) == n and n != 1 

times = int(raw_input())

for i in range(times):
	number = int(raw_input())
	if(check_divisor(number)):
		print "%d eh perfeito" % number
	else:
		print "%d nao eh perfeito" % number
