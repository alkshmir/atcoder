N, M = [int(s) for s in input().split()]
B = []
for _ in range(N):
    B.append([int(s) for s in input().split()])

for i in range(N):
    for j in range(M):
        # 右
        if j+1 < M and (B[i][j] + 1 != B[i][j+1] or (B[i][j]%7 == 0 and B[i][j+1]%7 == 1)):
            print("No")
            exit()
        # 下
        if i+1 < N and B[i][j] + 7 != B[i+1][j]:
            print("No")
            exit()
print("Yes")
