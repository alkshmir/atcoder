# たてには置けないので各行で左からTTの組み合わせをPCにおきかえていけばいい

H, W = [int(s) for s in input().split()]
S = []
for _ in range(H):
    S.append([c for c in input()])

for i in range(H):
    for j in range(W-1):
        if S[i][j] == 'T' and S[i][j+1] == "T":
            S[i][j] = "P"
            S[i][j+1] = "C"

for i in range(H):
    print("".join(S[i]))