# BFS
from collections import deque, defaultdict

visited = defaultdict(bool)
que = deque()

N = int(input())
A = [int(s) for s in input().split()]
M = int(input())
B = set([int(s) for s in input().split()])
X = int(input())

que.appendleft(0)
while len(que):
    v = que.popleft()
    if v == X:
        print("Yes")
        exit()
    if v > X:
        continue
    # 次の行き先を決める
    #dest = [v + i for i in range(1, N+1)]
    dest = []
    for i in A:
        if v + i in B:
            continue
        dest.append(v + i)
    #print(v, dest)
    for d in dest:
        if visited[d]:
            continue
        visited[d] = True
        que.append(d)
print("No")