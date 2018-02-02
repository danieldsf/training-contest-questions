cont = 0
amount = 0.0

while(True):
	try:
		line = raw_input()
		number = float(raw_input())
		cont += 1
		amount += number
	except EOFError:
		print "%.1f" % (amount / cont)
		break
