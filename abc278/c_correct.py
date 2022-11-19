N, Q = [int(s) for s in input().split()]
T = []
A = []
B = []
for _ in range(Q):
    t, a, b = [int(s) for s in input().split()]
    T.append(t)
    A.append(a)
    B.append(b)

#follows = [set() for _ in range(N+1)]
follows = set()

for t, a, b in zip(T, A, B):
    if t == 1:
        follows.add((a, b))
    elif t == 2:
        follows.discard((a, b))
    elif t == 3:
        if (a, b) in follows and (b, a) in follows:
            print("Yes")
        else:
            print("No")
