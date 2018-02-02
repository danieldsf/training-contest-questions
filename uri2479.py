number = input()
cont_good = 0
names = []
for i in range(number):
	s, name = raw_input().split()
	names.append(name)
	
	if(s == '+'):
		cont_good += 1
	
names.sort()
for n in names:
	print n
print "Se comportaram: %d | Nao se comportaram: %d" % (cont_good, number - cont_good)
