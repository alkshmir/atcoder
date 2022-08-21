h, w = [int(s) for s in input().split()]
G = []
for _ in range(h):
    G.append(list(input()))

coor = (0, 0)
rireki = set()
while(True):
    if coor in rireki:
        print(-1)
        exit()

    rireki.add(coor)

    Gij = G[coor[0]][coor[1]]
    if Gij == 'U' and coor[0] != 0:
        coor = (coor[0]-1, coor[1])
    elif Gij == 'D' and coor[0] != h-1:
        coor = (coor[0]+1, coor[1])
    elif Gij == 'L' and coor[1] != 0:
        coor = (coor[0], coor[1]-1)
    elif Gij == 'R' and coor[1] != w-1:
        coor = (coor[0], coor[1]+1)
    else:
        break

print(coor[0]+1, coor[1]+1)