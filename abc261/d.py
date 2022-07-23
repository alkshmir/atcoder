#import numpy as np
N, M = [int(s) for s in input().split()]
X = [int(s) for s in input().split()]
X = [0] + X
CY = [0 for _ in range(N+1)]
for _ in range(M):
    c, y = [int(s) for s in input().split()]
    CY[c] = y
#print(CY)
#dp = np.zeros((N+1, N+1))
dp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for c in range(1, i+1):
        dp[i][c] = dp[i-1][c-1] + X[i] + CY[c]

    dp[i][0] = max([dp[i-1][j] for j in range(i)] + [0])

ans = max([dp[N][j] for j in range(N+1)])

#print(dp)
print(int(ans))