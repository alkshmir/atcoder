import math
N, L, R = [int(s) for s in input().split()]
A = [0] + [int(s) for s in input().split()]

dp = [[[math.inf for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]

dp[1][0][0] = A[1]
for i in range(1, N):
    for j in range(1, i):
        for k in range(1, i):
            print(i, j , k)
            dp[i][0][0] = sum(A[1:i])
            dp[i][j][k+1] = min(dp[i][j][k], dp[i][j][k] - A[i-k]+R)
            dp[i][j+1][k] = min(dp[i][j][k], dp[i][j][k] - A[j] + L)
            dp[i+1][j][k] = min(dp[i][j][0]+A[i+1], dp[i][j][k]+R)

print(dp) 