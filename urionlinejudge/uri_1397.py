
while(True):
	times = int(raw_input())
	if(times == 0):
		break
	qtd_a, qtd_b = 0,0
	for i in range(times):
		a,b = map(int, raw_input().split())
		if(a > b):
			qtd_a += 1
		elif(a < b):
			qtd_b += 1
		
	print qtd_a,qtd_b
