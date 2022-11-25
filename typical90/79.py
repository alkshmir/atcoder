H, W = [int(s) for s in input().split()]
A = []
B = []
for _ in range(H):
    A.append([int(s) for s in input().split()])
for _ in range(H):
    B.append([int(s) for s in input().split()])
diff = []
for i in range(H):
    diff.append([b-a for b, a in zip(B[i], A[i])])

cnt = 0
for h in range(H-1):
    for w in range(W-1):
        tmp = diff[h][w]
        diff[h][w] = 0
        diff[h][w+1] -= tmp
        diff[h+1][w] -= tmp
        diff[h+1][w+1] -= tmp
        cnt += abs(tmp)

for h in range(H):
    for w in range(W):
        if diff[h][w] != 0:
            print("No")
            exit()
print("Yes")
print(cnt)