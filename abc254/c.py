
N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

ans = sorted(A)

mods = []
for k in range(K):
    mods.append(sorted(A[k::K]))
    
#print(mods)

tmp = []
for i in range(N):
    tmp.append(mods[(i % K)][int(i/K)])
#print(tmp)
if tmp == ans:
    print("Yes")
else:
    print("No")