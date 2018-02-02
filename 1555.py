times = int(raw_input())

def winner(x,y):
	eq_rafael = (3*x)**2 + y**2
	eq_beto = 2*(x**2) + (5*y)**2
	eq_carlos = y**3 - 100*x
	
	if(eq_beto > eq_carlos and eq_beto > eq_rafael):
		return "Beto"
	elif(eq_rafael > eq_carlos and eq_rafael > eq_beto):
		return "Rafael"
		
	return "Carlos"

for i in range(times):
	xy = map(int, raw_input().split())
	print "%s ganhou" % winner(xy[0], xy[1])
