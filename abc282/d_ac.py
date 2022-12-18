from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)

# 二部グラフ判定
def dfs(v) -> bool:
    visited[v] = True
    for dest in node[v]:
        if not visited[dest]:
            color[dest] = not color[v]
            if not dfs(dest):
                return False
        else:
            if color[dest] == color[v]:
                return False
    return True

N, M = [int(s) for s in input().split()]
node = defaultdict(list)
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    # zero indexed
    node[u-1].append(v-1)
    node[v-1].append(u-1)

visited = [False for _ in range(N)]
color = dict()
renketsu = 0 # 連結成分の個数
zero = False
cnt = N*(N-1) // 2 - M
color[0] = True
for i in range(N):
    if visited[i]:
        continue
    color = dict()
    color[i] = True
    if not dfs(i):
        zero = True
        break
    renketsu += 1

    # 各連結成分で二部グラフかどうかを確かめる
    # 黒に塗られている頂点の数
    black = 0
    white = 0
    for k, v in color.items():
        if v:
            black += 1
        else:
            white += 1
    cnt -= black*(black-1)//2
    cnt -= white*(white-1)//2

if zero:
    print(0)
else:
    print(cnt)