#fatorial

def fat(n):
	res = 1
	for i in range(2,n+1):
		res = res*i
	return res

print(fat(5))