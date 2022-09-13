H, W = [int(s) for s in input().split()]
S = []
for _ in range(H):
    S.append(input())

koma = []
for h in range(H):
    for w in range(W):
        if S[h][w] == 'o':
            koma.append((h, w))

print(abs(koma[0][0] - koma[1][0]) + abs(koma[0][1] - koma[1][1]))
