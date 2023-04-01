# BFSしようと思ったけど格子点が10^10個ぐらいあるから無理じゃね？

# BFS

from collections import deque, defaultdict

grid_points = set()
s = [int(s) for s in input().split()]
t = [int(t) for t in input().split()]
a, b, c, d = [int(s) for s in input().split()]

for x in range(a, b+1):
    for y in range(c, d+1):
        grid_points.add((x, y))

que = deque()
que.append((s[0], s[1]))
visited = defaultdict(bool)
visited[(s[0], s[1])] = True
depth = 0
while(len(que) and depth <= 10**6 ):
    v = que.popleft()
    if v[0] == t[0] and v[1] == t[1]:
        print("Yes")
        
    # 次の行き先
    dest = []
    for xg, yg in grid_points:
        x = xg - v[0]
        y = yg - v[1]
        dest.append((v[0]+2*x, v[1]+2*y))
    
    for d in dest:
        if visited[d]:
            continue
        visited[d] = True
        que.append(d)
    depth += 1

