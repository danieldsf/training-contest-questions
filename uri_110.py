def cards(n):
	l_card = range(1,n+1)
	discard = []
	while(len(l_card) > 1):
		discard.append(l_card.pop(0))
		l_card.append(l_card.pop(0))
	return discard, l_card[0]

def format_output(discard):
	print "Discarded cards:",
	for i in range(len(discard)):
		if(i < len(discard) - 1):
			print "%d," % discard[i],
		else:
			print discard[i]
	

while(True):
	times = input()
	if(times == 0):
		break
	
	ld, rem = cards(times)
	format_output(ld)
	print "Remaining card: %d" % rem
	
	
