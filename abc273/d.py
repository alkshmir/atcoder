H, W, rs, cs = [int(s) for s in input().split()]
N = int(input())
r = []
s = []
for _ in range(N):
    tmp = [int(s) for s in input().split()]
    r.append(tmp[0])
    s.append(tmp[1])

Q = int(input())
d = []
l = []
for _ in range(Q):
    tmp = [s for s in input().split()]
    d.append(tmp[0])
    l.append(int(tmp[1]))



# kabe
kabe = set([(x,y) for x,y in zip(s, r)])


x = cs
y = rs
for i in range(Q):
    for _ in range(l[i]):
        if d[i] == 'L':
            if (x-1, y) in kabe or x ==1:
                pass
            else:
                x -= 1
        elif d[i] == 'R':
            if (x+1, y) in kabe or x == W:
                pass
            else:
                x += 1
        elif d[i] == 'U':
            if (x, y-1) in kabe or y == 1:
                pass
            else:
                y -= 1
        else:
            if (x, y+1) in kabe or y == H:
                pass
            else:
                y += 1
    print(y, x)
