import re

times = int(raw_input())

for i in range(times):
	letter = raw_input()
	if(len(letter) == 5):
		print 3
	elif(re.match( r'(.*)ne', letter) or re.match( r'o(.*)e', letter) or re.match( r'on(.*)', letter)):
		print 1
	else:
		print 2
