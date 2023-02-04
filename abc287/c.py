# 辺を1つしかもたない頂点を始点としてDFSした時に同じ頂点を訪問しない、かつ全ての頂点を訪問する
from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)

def dfs(v, prev):
    visited[v] = True
    if len(nodes[v]) >= 3:
        print("No")
        exit()
    for dest in nodes[v]:
        if dest == prev:
            continue
        if visited[dest]:
            print("No")
            exit()
        dfs(dest, v)

N, M = [int(s) for s in input().split()]
if N != M+1:
    print("No")
    exit()
nodes = defaultdict(list)
visited = [False for _ in range(N+1)]
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    nodes[u].append(v)
    nodes[v].append(u)

valid = False
for k, v in nodes.items():
    if len(v) == 1:
        start = k
        valid = True
        break
if not valid:
    print("No")
    exit()

dfs(start, start)
for n in range(1, N+1):
    if not visited[n]:
        print("No")
        exit()
print("Yes")