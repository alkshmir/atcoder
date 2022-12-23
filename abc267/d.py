N, M = [int(s) for s in input().split()]
A = [None] + [int(s) for s in input().split()]

# dp[i][j]をAのi個目の要素までをj個使って作れる最大値とおく(j<=i)
# dp[i][i]はAのiこめまでのi*A[i]の和である
# dp[i+1][j+1]はA[i+1]を使う場合と使わない場合を考えてmax(dp[i][j+1], dp[i][j] + j*A[i+1])
# 求める数はdp[N][M]
import math
dp = [[-math.inf for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
#for i in range(M):
#    dp[i+1][i+1] = dp[i][i] + i*A[i]
#print(dp)
for i in range(N):
    for j in range(min(M, i+1)):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + (j+1)*A[i+1])
        #dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + (i+1)*A[i+1])
        #print(i+1, j+1, dp[i][j+1], dp[i][j] + (i+1)*A[i], dp[i+1][j+1])
#print(dp)
print(dp[N][M])