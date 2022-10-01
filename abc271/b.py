N, Q = [int(s) for s in input().split()]

a =[]
L = []
for _ in range(N):
    tmp = [int(s) for s in input().split()]
    L.append(tmp[0])
    a.append(tmp[1:])

#s = []
#t = []
for _ in range(Q):
    tmp = [int(s) for s in input().split()]
    
    #s.append(tmp[0])
    #t.append(tmp[1])
    s = tmp[0]
    t = tmp[1]
    print(a[s-1][t-1])
