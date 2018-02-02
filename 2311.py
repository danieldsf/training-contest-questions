times = int(raw_input())

names, points = [], []

for i in range(times):
	names.append(raw_input())
	weight = float(raw_input())
	temp_points = map(float, raw_input().split())
	points.append(weight * (sum(temp_points) - min(temp_points) - max(temp_points)))

for i in range(len(names)):
	print "%s %.2f" % (names[i], points[i])	
