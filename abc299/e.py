from collections import defaultdict, deque

N, M = [int(s) for s in input().split()]

nodes = defaultdict(list)
dist = [[N+1 for _ in range(N)] for _ in range(N)]
for n in range(N):
    dist[n][n] = 0

for _ in range(M):
    u, v = [int(s) for s in input().split()]
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)
    dist[u-1][v-1] = 1
    dist[v-1][u-1] = 1

K = int(input())

# BFSで2頂点間の距離を調べる
for n in range(N):
    que = deque()
    que.append(n)
    visited = [False for _ in range(N)]
    visited[n] = True
    while len(que) > 0:
        v = que.popleft()
        for d in nodes[v]:
            if visited[d]:
                continue
            visited[d] = True
            dist[n][d] = min(dist[n][d], dist[n][v]+1)
            que.append(d)

# すべて黒で塗ったあと、
# pi から di 未満の頂点をすべて白で塗る
color = [1 for _ in range(N)]

P = []
D = []
# O(NK)
for _ in range(K):
    p, d = [int(s) for s in input().split()]
    p -= 1
    P.append(p)
    D.append(d)
    for n in range(N):
        # pi からの距離が di 未満の頂点をすべて白で塗る
        if dist[p][n] < d:
            color[n] = 0
    
# 1 つ以上の黒い頂点が 存在する。
if 1 not in color:
    print("No")
    exit()

# すべての i = 1, ..., Kにおいてpiから距離がdi以下の黒い頂点が存在する
for i in range(K):
    flag = False
    for n in range(N):
        if dist[P[i]][n] <= D[i] and color[n] == 1:
            flag = True
            break
    if flag == False:
        print("No")
        exit()
print("Yes")
print(''.join([str(i) for i in color]))