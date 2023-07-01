# BFS

from collections import deque

# input
H, W = [int(s) for s in input().split()]
S = []
for _ in range(H):
    S.append([str(s) for s in input()])

if S[0][0] != 's':
    print("No")
    exit()

snuke = ['s', 'n', 'u', 'k', 'e']
visited = [[False for _ in range(W)] for _ in range(H)]
que = deque()
que.append((0, 0))
visited[0][0] = True
depth = 0
found = False
#cnt = 0
while len(que):
    dest = []
    # 次の行き先を決める
    while len(que):
        h_now, w_now = que.popleft()
        nxt = []
        if h_now != 0:
            nxt.append((h_now-1, w_now))
        if h_now != H-1:
            nxt.append((h_now+1, w_now))
        if w_now != 0:
            nxt.append((h_now, w_now-1))
        if w_now != W-1:
            nxt.append((h_now, w_now+1))
        for v in nxt:
            if S[v[0]][v[1]] == snuke[(depth+1)%5]:
                dest.append(v)
    #print("depth: ", depth)
    #print(depth, dest)
    for d in dest:
        if visited[d[0]][d[1]]:
            continue
        #print(d)
        visited[d[0]][d[1]] = True
        if d == (H-1, W-1):
            found = True
            break
        que.append(d)
    depth += 1

if found:
    print("Yes")
else:
    print("No")
