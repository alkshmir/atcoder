H, W = [int(s) for s in input().split()]
C = []
for _ in range(H):
    C.append(list(input()))

ans = []
for j in range(W):
    cnt = 0
    for i in range(H):
        
        if C[i][j] == '#':
            cnt += 1
    ans.append(str(cnt))
print(' '.join(ans))