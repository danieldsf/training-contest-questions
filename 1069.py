times = int(raw_input())

for i in range(times):
	new_word = ""
	word = raw_input()
	distance = int(raw_input())
	for i in word:
		position = ord(i)
		if((position - distance) >= 65):
			new_word += chr(position - distance)
		else:
			new_word += chr(90 - (distance - (position - 64)))
	print new_word

#65 -> 90
