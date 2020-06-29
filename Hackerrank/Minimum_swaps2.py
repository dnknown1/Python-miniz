def minswap2(Q):
    count = 0
    while not Q == list(range(1, len(Q)+1)):
        for i, v in enumerate(Q):
            if not i == (v-1):
                #k = Q.index(i+1)
                Q[i], Q[v-1] = Q[v-1], Q[i]
                count += 1
    return count

a =[[4,3,1,2], [4,2,3,1],[1, 3, 5, 2,4, 6, 7],]

for _ in range(len(a)):
    print(a[0])
    print(minswap2(a.pop(0)))