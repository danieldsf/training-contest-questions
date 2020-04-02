
vector = []

while(True):
	a = int(input())
	if(a == 0):
		break
	temp = []
	
	for i in range(a):
		temp.append(map(int, input().split()))
	
	vector.append(temp)

print(vector)
		
