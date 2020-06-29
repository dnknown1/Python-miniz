from collections import defaultdict


frq = defaultdict(int)

def freqQuery(q):
    global frq
    print(frq)
    if q[0] == 1:
        frq[q[1]] += 1
    
    if q[0] == 2:
        frq[q[1]] -= 1
    
    if q[0] == 3:
        for v in frq.values():
            if v == q[1]:
                return 1
        return 0

q = 10 #int(input())
queries = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5],[1, 5],[1, 4],[3, 2],[2, 4], [3, 2]]
#list()
for k in range(len(q)):
    #a = freqQuery(list(map(int, input().split())))
    a = freqQuery(queries(k))
    if not a == None:
        print(a)
