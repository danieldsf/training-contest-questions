times = int(raw_input())

for i in range(times):
	expression = raw_input()
	a,b = int(expression[0]), int(expression[2])
	letter = expression[1]
	if(a == b):
		print a * b
	elif(letter.isupper()):
		print b - a
	else:
		print a + b
		
