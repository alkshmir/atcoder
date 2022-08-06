import math
N, L, R = [int(s) for s in input().split()]
A = [0] + [int(s) for s in input().split()]

f = [math.inf for _ in range(N+1)]
g = [math.inf for _ in range(N+1)]

f[0] = 0
f[1] = min(A[1], L)
for i in range(1, N):
    f[i+1] = min(f[i] + A[i+1], L*(i+1))

g[0] = 0
g[1] = min(A[N], R)
for i in range(1, N):
    g[i+1] = min(g[i] + A[N-i], R*(i+1))

#print(f)
#print(g)
print(min([f[i] + g[N-i] for i in range(N+1)]))