from collections import defaultdict
import sys

sys.setrecursionlimit(2000000)

N = int(input())
A = []
B = []
node = defaultdict(list)

max_rank = 1
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)
    node[a].append(b)
    node[b].append(a)
    max_rank = max(max_rank, b)

visited = defaultdict(bool)
to_visit = [node[1]]

def dfs(v):
    visited[v] = True
    for dest in node[v]:
        if visited[dest]:
            continue
        dfs(dest)
    
dfs(1)
rank = 1
for k, v in visited.items():
    if v:
        rank = max(rank, k)
print(rank)