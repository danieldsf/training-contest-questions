def pair(word):
	full_pair = 0
	op_pair = 0
	for i in word:
		if(i == '>'):
			if(op_pair > 0):
				full_pair += 1
				op_pair -= 1
		if(i == '<'):
			op_pair += 1
	return full_pair
	
times = input()

for i in range(times):
	n = raw_input()
	print pair(n)
