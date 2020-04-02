def fim_comida(qtd):
	qtd_dias = 0
	if(qtd < 1):
		return 1

	while(True):
		if(qtd < 1.0):
			break
		qtd_dias += 1
		qtd /= 2
		
	return qtd_dias

n = input()

for i in range(n):
	valor = float(raw_input())
	print "%d dias" % fim_comida(valor) 
