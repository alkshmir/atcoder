# BFS
from collections import deque

a, N = [int(s) for s in input().split()]
max_n = 10**len(str(N))
visited = [False for _ in range(max_n)]
que = deque()
que.append(1)
visited[1] = True
depth = 0
found = False
while len(que) and not found:
    dest = []
    while len(que):
        v = que.popleft()
        # Multiply
        if a*v < max_n:
            dest.append(a*v)
        # Rotate
        if v >= 10 and v%10 != 0:
            tmp = str(v)
            tmp = tmp[-1] + tmp[:-1]
            dest.append(int(tmp))
    #print("depth: ", depth)
    for d in dest:
        if visited[d]:
            continue
        #print(d)
        visited[d] = True
        if d == N:
            found = True
            break
        que.append(d)
    depth += 1

if found:
    print(depth)
else:
    print(-1)
