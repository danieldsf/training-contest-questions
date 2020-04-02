times = input()

numbers = map(int, raw_input().split())

less = numbers[0]
index = 0

for i in range(1, times):
	if(less > numbers[i]):
		less = numbers[i]
		index = i
		
print index+1
