times = input()

for i in range(times):
	n_prod = input()
	things = dict()
	for j in range(n_prod):
		name, value = raw_input().split()
		things[name] = float(value)
	total = 0.0
	n_things = input()
	for j in range(n_things):
		name, qtd = raw_input().split()
		total += things[name] * int(qtd)
	print "R$ %.2f" % total
