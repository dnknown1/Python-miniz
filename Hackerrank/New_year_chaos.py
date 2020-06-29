# bribes a person and swaps position
def bribe(q, k):
    loc = q.index(k)
    q[loc], q[loc -1] = q[loc -1], q[loc]
    
# minimum bribes required 
def min_bribe(N, Q):
    eQ = list(range(1, N+1))
    total_bribe = 0
    for i in range(N):
        if not Q[i] == eQ[i]:
            # index of key in expected queue
            eki = eQ.index(Q[i])
            # bribes needed to be in this position
            b = abs(eki - i)
            if b <= 2:
                total_bribe += b
                for j in range(b):
                    bribe(eQ, Q[i])
            else:
                return 'Too chaotic'
    return total_bribe

if __name__ == '__main__':
    t = int(input())
    ns = list()
    qs = list()
    for _ in range(t):
        ns.append(int(input()))
        qs.append(list(map(int, input().split())))
    for _ in range(t):
        print(min_bribe(ns.pop(0), qs.pop(0)))


# better soln
'''
def mbribe(q):
    moves = 0
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            return "Too chaotic"
        for j in range(max(0,val-2), pos):
            if q[j] > val:
                moves+=1
    return moves
'''