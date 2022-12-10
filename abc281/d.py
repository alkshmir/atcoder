N, K, D = [int(s) for s in input().split()]
A = [0] + [int(s) for s in input().split()]

dp = [[[-1 for _ in range(D)] for _ in range(K+1)] for _ in range(N+1)]

dp[1][0][0] = 0
dp[1][1] = [A[1] if k==A[1]%D else -1 for k in range(D) ]
for i in range(1, N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1: # XXX
                continue
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

            if j<K:
                dp[i+1][j+1][(k+A[i+1])%D] = max(dp[i+1][j+1][(k+A[i+1])%D], dp[i][j][k] + A[i+1])
#print(dp)

print(dp[N][K][0])