a = 1
while a <= 100:	
	m = a % 7
	n = a % 10
	t = a // 10	
	if m == 0 or n == 7 or t == 7:	
		a += 1	
	else:
		print(a)	
		a += 1