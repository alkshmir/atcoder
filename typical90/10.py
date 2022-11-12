N = int(input())
C = [None]
P = [None]
for _ in range(N):
    c, p = [int(s) for s in input().split()]
    C.append(c)
    P.append(p)
Q = int(input())
L = []
R = []
for _ in range(Q):
    l, r = [int(s) for s in input().split()]
    L.append(l)
    R.append(r)

cum_sum = {1: [0], 2: [0]}
for i in range(1, N+1):
    if C[i] == 1:
        cum_sum[1].append(cum_sum[1][-1] + P[i])
        cum_sum[2].append(cum_sum[2][-1])

    else:
        cum_sum[2].append(cum_sum[2][-1] + P[i])
        cum_sum[1].append(cum_sum[1][-1])

#print(cum_sum[1], cum_sum[2])

for l, r in zip(L, R):
    print(cum_sum[1][r] - cum_sum[1][l-1], cum_sum[2][r] - cum_sum[2][l-1])
