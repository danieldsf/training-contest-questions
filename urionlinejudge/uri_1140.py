def tautogram(word):
	letter = word[0]
	list_char = word.split()
	flag = 'Y'
	for i in list_char:
		if(letter != i[0]):
			flag = 'N'
	return flag
	
while(True):
	phrase = raw_input().upper()
	if(phrase == "*"):
		break
	print tautogram(phrase)
