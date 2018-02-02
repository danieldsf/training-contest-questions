
vector = []

while(True):
	a = int(raw_input())
	if(a == 0):
		break
	temp = []
	
	for i in range(a):
		temp.append(map(int, raw_input().split()))
	
	vector.append(temp)

print vector
		
