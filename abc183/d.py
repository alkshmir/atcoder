#imos法

N, W = [int(s) for s in input().split()]
S = []
T = []
P = []
for _ in range(N):
    s, t, p = [int(s) for s in input().split()]
    S.append(s)
    T.append(t)
    P.append(p)

maxT = max(T)
table = [0 for _ in range(maxT+1)]

for s, t, p in zip(S, T, P):
    table[s] += p
    table[t] -= p

# simulation
for t in range(maxT+1):
    if t > 0:
        table[t] += table[t-1]

max_vol = max(table)

if max_vol > W:
    print("No")
else:
    print("Yes")