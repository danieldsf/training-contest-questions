# -*- coding: utf-8 -*-

cont_gi, qtd_g, qtd_i, qtd_em = 0, 0, 0, 0 

while(True):
	pi, pg = map(int, raw_input().split())
	cont_gi += 1

	if(pg == pi):
		qtd_em += 1
	
	if(pg > pi):
		qtd_g += 1
		
	if(pg < pi):
		qtd_i += 1

	sair = int(raw_input("Novo grenal (1-sim 2-nao)"))
	if(sair == 2):
		break

#Impressao dos resultados:
print "%d grenais" % cont_gi
print "Inter:%d" % qtd_i
print "Gremio:%d" % qtd_g
print "Empates:%d" % qtd_em

if(qtd_g > qtd_i):
	print "Gremio venceu mais"
elif(qtd_i > qtd_g):
	print "Inter venceu mais"
else:
	print "Nao houve vencedor"
