"""Problem: A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly several times, where each move is a standard knight move. If the knight jumps off the board at any point, however, it is not allowed to jump back on.
    After k moves, what is the probability that the knight remains on the board?
"""


# Returns all the valid moves
def moves(loc):
    # TODO: write code...
    lands = list()
    
    if (loc[0]-2 >= 0) and (loc[1]-1 >= 0):
        lands.append((loc[0]-2, loc[1]-1))
    
    if (loc[0]-1 >= 0) and (loc[1]-2 >= 0):
        lands.append((loc[0]-1, loc[1]-2))
    
    if (loc[0]-2 >= 0) and (loc[1]+1 <= 7):
        lands.append((loc[0]-2, loc[1]+1))
    
    if (loc[0]+2 <= 7) and (loc[1]-1 >= 0):
        lands.append((loc[0]+2, loc[1]-1))
    
    if (loc[0]+2 <= 7) and (loc[1]+1 <= 7):
        lands.append((loc[0]+2, loc[1]+1))
    
    if (loc[0]-1 >= 0) and (loc[1]+2 <= 7):
        lands.append((loc[0]-1, loc[1]+2))
    
    if (loc[0]+1 <= 7) and (loc[1]+2 <= 7):
        lands.append((loc[0]+1, loc[1]+2))
    
    if (loc[0]+1 <= 7) and (loc[1]-2 >= 0):
        lands.append((loc[0]+1, loc[1]-2))
    
    return lands


# returns all valid landings after k'th step 
def landings(loc, k):
    m = list()
    if k == 1:
        #print(len(m))
        return moves(loc)
    
    for l in moves(loc):
        m += landings(l,k-1)
    return m


# finds probsbility
def probab(loc, k):
    return len(landings(loc, k))/(8 if k==1 else 8*len(landings(loc, k-1)))
    


# driver
if __name__ == '__main__':
    loc = tuple(map(int,input().split()))
    k = int(input())
    
    if loc[0]>0 and loc[1]>=0 and loc[0]<=7 and loc[1]<=7:
        print(probab(loc, k))
    else:
        print('Incorrect position')
