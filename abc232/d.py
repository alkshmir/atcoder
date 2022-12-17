# 普通のDFS ABC277 C問題が類題かな
# グラフを自分で書かないといけないのが他の問題とやや違うところか
# 計算量はO(HW)
# 解説読んだら全然DFSじゃなかった…
from collections import defaultdict
import sys

sys.setrecursionlimit(2000000)

H, W = [int(s) for s in input().split()]
C = []
for _ in range(H):
    C.append(input())

next = defaultdict(list)
visited = defaultdict(bool)

def dfs(v):
    visited[v] = True
    for dest in next[v]:
        if visited[dest]:
            continue
        dfs(dest)

for i in range(H):
    for j in range(W):
        if i+1 < H and C[i+1][j] == '.':
            next[(i, j)].append((i+1, j))
        if j+1 < W and C[i][j+1] == '.':
            next[(i, j)].append((i, j+1))
#print(next)
dfs((0, 0))
#print(visited)
ans = 1
for k, v in visited.items():
    if v:
        ans = max(ans, k[0] + k[1] + 1)
print(ans)