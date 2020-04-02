times = input()

for i in range(times):
	x,y = map(int, raw_input().split())
	print "%d cm2" % (x * y / 2)
