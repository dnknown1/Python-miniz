
def count_valleys(p):
	at = 0
	count = 0
	for i in range(len(p)-1):
		at = at-1 if p[i].lower() == 'd' else at+1
		if p[i+1].lower() == 'u' and at+1 == 0:
			count += 1
	return count

input()
print(count_valleys(input()))
