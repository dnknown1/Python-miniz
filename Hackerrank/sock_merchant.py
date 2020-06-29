'''John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n socks with colors c[n]. There is k pair of color c[i],   and h of color c[j] . There are x odd socks left, one of each color. The number of pairs k+h'''

def sock_merchant(c) :
	srt = dict()
	count = 0
	for i in c:
		if i in srt.keys():
			srt[i] += 1
		else:
			srt[i] = 1
		if srt[i] % 2 == 0:
				count +=1
	return count

n = input()
print(sock_merchant(input().split()))