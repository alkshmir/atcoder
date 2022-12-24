from collections import defaultdict
import sys

sys.setrecursionlimit(2000000)

N, M = [int(s) for s in input().split()]

node = defaultdict(list)
for _ in range(M):
    a, b = [int(s) for s in input().split()]
    node[a].append(b)

visited = defaultdict(bool)

def dfs(v):
    visited[v] = True
    for dest in node[v]:
        if visited[dest]:
            continue
        dfs(dest)

cnt = 0
for i in range(1, N+1):
    visited = defaultdict(bool)
    dfs(i)
    cnt += sum([v for v in visited.values()])
print(cnt)