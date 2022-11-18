N, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
L = []
R = []
V = []
for _ in range(Q):
    l, r, v = [int(s) for s in input().split()]
    L.append(l)
    R.append(r)
    V.append(v)

e = 0
diff = [0]
for i in range(N-1):
    e += abs(A[i]-A[i+1])
    diff.append(A[i+1] - A[i])

for l, r, v in zip(L, R, V):
    if l != 1:
        tmp = diff[l-1]
        diff[l-1] += v
        e += abs(diff[l-1]) - abs(tmp)
    if r != N:
        tmp = diff[r]
        diff[r] -= v
        e += abs(diff[r]) - abs(tmp)
    print(e)