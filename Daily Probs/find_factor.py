def found_fact(n):
	l = list()
	for i in range(2,n):
		tmp = n%i 
		if not tmp:
			l.append(i)
	return l
for i in {29,341,129,67,221}:
	print(i,found_fact(i))