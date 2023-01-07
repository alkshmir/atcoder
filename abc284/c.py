from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)

N, M = [int(s) for s in input().split()]
node = defaultdict(list)
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    node[u-1].append(v-1)
    node[v-1].append(u-1)

def dfs(v):
    visited[v] = True
    for dest in node[v]:
        if visited[dest]:
            continue
        dfs(dest)
    
visited = [False for _ in range(N)]
renketsu = 0
for i in range(N):
    if visited[i]:
        continue
    dfs(i)
    renketsu += 1
print(renketsu)