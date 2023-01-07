from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)

N, M = [int(s) for s in input().split()]
node = defaultdict(list)
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    node[u].append(v)
    node[v].append(u)

visited = [False for _ in range(N+1)]

def dfs(v):
    visited[v] = True
    count = 0
    for dest in node[v]:
        if visited[dest]:
            continue
        count += dfs(dest)
        if count >= 10**6:
            break
    visited[v] = False
    return count + 1
print(min(dfs(1), 10**6))
