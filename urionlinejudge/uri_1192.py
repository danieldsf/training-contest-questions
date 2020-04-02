def op(a, sign, b):
	if(a == b):
		return a * b
	else:
		if(sign.isupper()):
			return b - a
		else:
			return a + b

times = input()

for i in range(times):
	word = raw_input()
	a,sign,b = word
	print op(int(a), sign, int(b))
