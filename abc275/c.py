import itertools
import numpy as np

S = []
for _ in range(9):
    S.append(input())

sharps = set()
#sharps_np = []
for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            sharps.add((i,j))
            #sharps_np.append(np.array([i,j]))

def swap(a):
    #return np.array([a[1], -a[0]])
    return (a[1], -a[0])

def plus(a, b):
    return (a[0]+b[0], a[1]+b[1])

def minus(a, b):
    return (a[0]-b[0], a[1]-b[1])

def eq(a,b):
    return a[0] == b[0] and a[1] == b[1]
#def np2tup(n):
#    return (int(n[0]), int(n[1]))
def isIsoscelesRightTriangle(a, b, c):
    # a 直角
    #ba = a - b
    ba = minus(a, b)
    sba = swap(ba)
    #if np.all((a + swap(ba))== c) or np.all((a - swap(ba)) == c):
    if eq(plus(a, sba), c) or eq(minus(a, sba), c):
        #return c - ba
        return minus(c, ba)
     
    # b 直角
    #ab = b - a
    ab = minus(b,a)
    sab = swap(ab)
    #if np.all((b + swap(ab)) == c) or np.all((b - swap(ab)) == c):
    if eq(plus(b,sab), c) or eq(minus(b, sab), c):
        #return c - ab
        return minus(c,ab)
    
    # c 直角
    #ac = c - a
    ac = minus(c, a)
    sac = swap(ac)
    #if np.all((c + swap(ac)) == b) or np.all((c - swap(ac)) == b):
    if eq(plus(c,sac), b) or eq(minus(c, sac), c):
        #return b - ac
        return minus(b, ac)
    return None

squares = set()
for sharp in itertools.combinations(sharps, 3): 
    # derive 4th cood

    d = isIsoscelesRightTriangle(sharp[0], sharp[1], sharp[2])

    if d is not None and d in sharps:
        #print([np2tup(sharp[0]), np2tup(sharp[1]), np2tup(sharp[2]), np2tup(d)])
        tmp_set = frozenset([sharp[0], sharp[1], sharp[2], d])
        squares.add(tmp_set)
        #print(squares)
#print(squares)
print(len(squares))