# A_iとA_N+1-iの関係をグラフ上の辺と見なし、値が異なる場合は頂点A_iとA_N+1-iに辺を張る
# 各連結成分では、登場する数の種類すなわち(頂点数-1)回の置換を行えば
# 各頂点を全て同じ数にできる
# よって、連結成分ごとに頂点数-1を足していけば良い

from collections import defaultdict
import sys
sys.setrecursionlimit(2000000)

def dfs(v):
    global cnt
    visited[v] = True
    cnt += 1
    for dest in node[v]:
        if visited[dest]:
            continue
        dfs(dest)

N = int(input())
A = [int(s) for s in input().split()]
node = defaultdict(set)
for i in range(N//2):
    #print(A[i], A[-i-1])
    if A[i] != A[-i-1]:
        node[A[i]].add(A[-i-1])
        node[A[-i-1]].add(A[i])

visited = defaultdict(bool)
ans = 0
for n in node.keys():
    if visited[n]:
        continue
    cnt = 0
    dfs(n)
    ans += cnt - 1
print(ans)