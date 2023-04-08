# 頂点xは実質頂点(x+N-1)%Nと考えてよい
# 考える行列もAだけで良い
# よって隣接行列AでできるグラフをBFSすればよい
# ただしs!=tでs%N == t%Nのとき自分自身に戻ってくる経路の長さを求める必要がある
# このとき、自分自身への距離は0という初期化を行うのではなく、
# 隣接なら距離1という初期化を行うことで回避する
from collections import deque, defaultdict
import math

N, K = [int(s) for s in input().split()]


node = defaultdict(list)

a = []
for i in range(N):
    #a.append([int(s) for s in input().split()])
    tmp = [int(s) for s in input().split()]
    for j, t in enumerate(tmp):
        if t == 1:
            node[i].append(j)
        
#print(node)

q = int(input())

for _ in range(q):
    s, t = [int(s) for s in input().split()]
    if s == t:
        print(0)
        continue
    s = (s-1) % N
    t = (t-1) % N

    visited = [False for _ in range(N)]
    distance = [math.inf for _ in range(N)]
    for e in node[s]:
        distance[e] = 1
    
    que = deque()
    que.append(s)
    
    #print (s, t)
    while len(que):
        v = que.popleft()
        for dest in node[v]:
            if visited[dest]:
                continue
            visited[dest] = True
            distance[dest] = min(distance[dest], distance[v]+1)
            que.append(dest)

    if distance[t] == math.inf:
        print(-1)
    else:
        print(distance[t]) 
