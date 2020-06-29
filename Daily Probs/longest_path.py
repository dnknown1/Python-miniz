'''Given a tree where each edge has a weight, compute the length of the longest path in the tree.
eg: 
nd the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.'''


#O(n^3)
#######	
def floyd_warshall(graph):
	n = len(graph)
	d = [[[infn for i in range(n)] for i in range(n)] for i in range(n+1)]
	d[0] = [i for i in graph]
	for k in range(n):
		#print('for k =',k,'\n',d[k])
		for i in range(n):
			for j in range(n):
				d[k+1][i][j]= min(d[k][i][j], d[k][i][k]+d[k][k][j])
	return (d[n])
    
#********#
infn = 9999
graph = [
		[0,3,5,8,infn,infn,infn,infn],
		[3,0,infn,infn,infn,infn,infn,infn],
		[5,infn,0,infn,infn,infn,infn,infn],
		[8,infn,infn,0,2,4,infn,infn],
		[infn,infn,infn,2,0,infn,1,1],
		[infn,infn,infn,4,infn,0,infn,infn],
		[infn,infn,infn,infn,1,infn,0,infn],
		[infn,infn,infn,infn,1,infn,infn,0]
	]
for _ in floyd_warshall(graph):
	print(*_)