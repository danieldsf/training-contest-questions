#UNDONE
while(True):
	number = input()
	xs, ys = [],[]
	status = 0 #0 => function, 1 => not revertble, 2 => not a function
	if(number == 0):
		break
	for i in range(number):
		listaxy = raw_input().split()
		x,y = listaxy[0], listaxy[2]
		if(x in xs):
			status = 2
		
		if(y in ys and status != 2):
			status = 1
		xs.append(x)
		ys.append(y)
	print ("Invertible.", "Not invertible.", "Not a function.")[status]

