import sys
from collections import defaultdict
sys.setrecursionlimit(2000000)
N = int(input())
nodes = set()
for _ in range(N):
    nodes.add(tuple([int(s) for s in input().split()]))
graph = defaultdict(list)

for x, y in nodes:
    for next in [(x-1, y-1), (x-1, y), (x, y-1), (x, y+1), (x+1, y), (x+1, y+1)]:
        if next in nodes:
            graph[(x, y)].append(next)

visited = defaultdict(bool)
def dfs(n):
    x, y = n
    visited[(x, y)] = True
    for dest in graph[(x, y)]:
        if visited[dest]:
            continue
        dfs(dest)

cnt = 0
for n in nodes:
    if visited[n]:
        continue
    dfs(n)
    cnt += 1

print(cnt)