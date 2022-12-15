import itertools
N, X = [int(s) for s in input().split()]
L = []
A = []
for _ in range(N):
    tmp = [int(s) for s in input().split()]
    L.append(tmp[0])
    A.append(tmp[1:])

cnt = 0
for p in itertools.product(*A):
    t = p[0]
    for i in range(1, len(p)):
        t *= p[i]
    #print(t)
    if t == X:
        cnt += 1
print(cnt)