import sys
from collections import deque
sys.setrecursionlimit(2000000)
N, M = [int(s) for s in input().split()]
visited = [[-1 for _ in range(N+1)] for _ in range(N+1)]
# 移動距離がsqrt(M)となる移動方法を求める
moves = set()
for k in range(N+1):
    for l in range(N+1):
        if k**2 + l**2 == M:
            moves.add((k, l))
            moves.add((-k, l))
            moves.add((k, -l))
            moves.add((-k, -l))
#print(moves)

# BFS
que = deque()
que.appendleft((1,1))
visited[1][1] = 0
while len(que):
    v = que.popleft()
    # 次の行き先を求める
    dest = []
    for x, y in moves:
        if 1 <= v[0] + x <=N and 1 <= v[1] + y <=N:
            dest.append((v[0]+x, v[1]+y))
    for d in dest:
        if visited[d[0]][d[1]] != -1:
            continue
        visited[d[0]][d[1]] = visited[v[0]][v[1]] + 1
        que.append((d[0], d[1]))

#print(visited)
for i in range(1, N+1):
    tmp = [str(visited[i][j]) for j in range(1, N+1)]
    print(' '.join(tmp))
        