odd, even = [], []

times = int(raw_input())

for i in range(times):
	number = int(raw_input())
	if(number % 2 == 0):
		even.append(number)
	else:
		odd.append(number)
		
odd.sort()
even.sort()

for i in even:
	print i

for i in range(len(odd)-1,-1,-1):
	print odd[i]


