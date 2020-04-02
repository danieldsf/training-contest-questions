
def generate_square(number):
	for i in range(number):
		line = []
		for j in range(number):
			line.append(2 ** (i+j))
		print linex

while(True):
	number = int(raw_input())
	if(number == 0):
		break
	generate_square(number)
