# iばんめのカードをひっくり返すときの可能な組み合わせをdp[i][0]
# ひっくり返さない時の可能な組み合わせをdp[i][1]とおく
# dp[i+1][0] = dp[i][1]*( B[i] != A[i+1]) + dp[i][0] * (A[i] != A[i+1])
# dp[i+1][1] = dp[i][1]*( B[i] != B[i+1]) + dp[i][0] * (A[i] != B[i+1])

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)

dp = [[0, 0] for _ in range(N+1)]

dp[1][0] = 1
dp[1][1] = 1

for i in range(1, N):
    dp[i+1][0] = (dp[i][1] * (B[i-1] != A[i]) + dp[i][0] * (A[i-1] != A[i]) )% 998244353 
    dp[i+1][1] = (dp[i][1] * (B[i-1] != B[i]) + dp[i][0] * (A[i-1] != B[i]) )% 998244353 

#print(dp[-1])
print(sum(dp[-1])% 998244353 )