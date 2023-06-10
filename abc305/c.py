H, W = [int(s) for s in input().split()]
S = []
for _ in range(H):
    S.append([s for s in input()])

a = H - 1
b = 0
d = 0
c = W - 1

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            a = min(a, h)
            b = max(b, h)
            c = min(c, w)
            d = max(d, w)

for h in range(a, b+1):
    for w in range(c, d+1):
        if S[h][w] == '.':
            print(h+1, w+1)
            exit()