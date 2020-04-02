
plug = map(int, raw_input().split())
tomada = map(int, raw_input().split())

possible = "Y"

for i in range(5):
	if(plug[i] + tomada[i] > 1):
		possible = "N"
		break
		
print possible
