# 特になにも意識することなく愚直に実装したらACだった
# 計算量はO(N!*N^2)だと思う。N=8なので間に合う。
import itertools
from collections import defaultdict
N, M = [int(s) for s in input().split()]
nodes_t = defaultdict(list)
nodes_a = defaultdict(list)
for _ in range(M):
    a, b = [int(s) for s in input().split()]
    nodes_t[a].append(b)
    nodes_t[b].append(a)
for _ in range(M):
    c, d = [int(s) for s in input().split()]
    nodes_a[c].append(d)
    nodes_a[d].append(c)

for p in itertools.permutations(range(1, N+1)):
    flag = True
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if not( (j in nodes_t[i] and p[j-1] in nodes_a[p[i-1]]) or \
                   (j not in nodes_t[i] and p[j-1] not in nodes_a[p[i-1]])):
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Yes")
        exit()
print("No")