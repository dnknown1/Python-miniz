def repeated_string(s,n):
	number=s.count('a')
	if number==0:
		return 0
	elif number==1 and len(s)==1:
		return n
	else:
		repeats=n//len(s)
		remainders=n%len(s)
		return int(number*repeats+s[:remainders].count('a'))       

s, n = input(), int(input())
print(repeated_string(s,n))