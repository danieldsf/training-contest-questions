while(True):
	times = int(raw_input())
	if(times == 0):
		break
	data = map(int, raw_input().split())
	print "Mary won %d times and John won %d times" % (data.count(0), data.count(1))


