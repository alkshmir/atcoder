#from collections import deque 
import sys

sys.setrecursionlimit(2000000)
def dfs():

    if len(to_visit) > 0 and to_visit[-1] == Y:
        print(*(to_visit))
        exit()
    now = to_visit[-1]
    for dest in edge[now]:
        if visited[dest]:
            continue
        to_visit.append(dest)
        visited[dest] = True
        dfs()
        to_visit.pop()

    return

N, X, Y = [int(s) for s in input().split()]
edge = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
#to_visit = deque()
to_visit = []

for _ in range(N-1):
    u, v = [int(s) for s in input().split()]
    edge[u].append(v)
    edge[v].append(u)

to_visit.append(X)
visited[X] = True
dfs()


