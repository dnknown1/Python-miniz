def fact(n):
	return n * fact(n-1) if n> 1 else 1

def permute_palindrome(s):
	for i in permute(s):
		if i == i[::-1]:
			return i
	return False

def permute(s):
	j = 0
	out= [s,]
	o = list(s)
	for i in range(fact(len(s))):
		o[j],o[j+1] = o[j+1],o[j]
		out.append(''.join(o))
		if j +1 < len(s)-1:
			j = j+1
		else:
			j = 0
	return out

s = 'carrace'
print(permute_palindrome(s))