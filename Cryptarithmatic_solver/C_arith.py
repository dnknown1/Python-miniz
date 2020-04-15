from itertools import permutations

# checks current permutation
def evaluate(ip,m):
	for i in ip:
		if m[i[0]] == 0:
			return False
	tmp=[]
	for i in ip:
		x = ''
		for j in i:
			x += str(m[j])
		tmp.append(int(x))
	return sum(tmp[:-1]) == tmp[-1]

# function to call	
def solve(ip):
	soln = list()
	n = range(10)
	fx = set(''.join(ip))
	# generates all possible permutations
	m = list(map(lambda p:dict(zip(fx,p)),permutations(n,len(fx))))
	# if finds a valid solution then appends to the list
	soln = list(filter(lambda p:evaluate(ip,p),m))
	return soln if len(soln) > 0 else False
