N, Q = [int(s) for s in input().split()]
T = []
A = []
B = []
for _ in range(Q):
    t, a, b = [int(s) for s in input().split()]
    T.append(t)
    A.append(a)
    B.append(b)

follows = [set() for _ in range(N+1)]

for t, a, b in zip(T, A, B):
    if t == 1:
        follows[a].add(b)
    elif t == 2:
        follows[a].discard(b)
    elif t == 3:
        if b in follows[a] and a in follows[b]:
            print("Yes")
        else:
            print("No")
