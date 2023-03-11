# 2**20 が10^6ぐらいなので全探索する。
import itertools
H, W = [int(s) for s in input().split()]
A = []
for _ in range(H):
    A.append([int(s) for s in input().split()])

cnt = 0
for h_idx in itertools.combinations(range(H+W-2), H-1):
    dir = [True for _ in range(H+W-2)]
    for i in h_idx:
        dir[i] = False
    
    pos_x = 0
    pos_y = 0
    history = set()
    history.add(A[0][0])
    valid = True
    #print(dir)
    for d in dir:
        if d:
            pos_y += 1
        else:
            pos_x += 1
        #print(pos_x, pos_y)
        if A[pos_x][pos_y] in history:
            valid = False
            break
        history.add(A[pos_x][pos_y])
    if valid:
        cnt += 1

print(cnt)