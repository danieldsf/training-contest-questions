list_answer = ['A', 'B', 'C', 'D', 'E']

while(True):
	times = input()
	if(times == 0):
		break
	for i in range(times):
		number_list = map(int, raw_input().split())
		#print number_list
		cont = 0
		position = 0
		for j in range(5):
			if(number_list[j] < 128):
				cont += 1
				position = j
		if(cont > 1):
			print "*"
		else:
			print list_answer[position]
				
			
