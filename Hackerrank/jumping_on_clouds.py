def jumping_on_clouds(i,a):
	jmps = 0
	while i < len(a):
		if i+2 < len(a) and a[i+2] != 1:
			i += 2
		elif i+1 < len(a) and a[i+1] != 1:
			i += 1
		else:
			break
		jmps +=1
	return jmps

_, a = input(), list(map(int,input().split()))
print(jumping_on_clouds(0,a))