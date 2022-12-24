# dp[i][k]をAをi個目まで使ったとき最終的な答えがkになる場合の数とする(i>=2)
# F operationをするときは、xがkになる場合の数は、dp[i][k]なので、
# dp[i+1][(k+A[i+1])%10]にdp[i][k]を加えればいい
# また、G operationをするときは、
# dp[i+1][(k*A[i+1])%10]にdp[i][k]を加えれば良い

N = int(input())
A = [None] + [int(s) for s in input().split()]
dp = [[0 for _ in range(10)] for _ in range(N+1)]

dp[2][(A[1] + A[2])%10] += 1
dp[2][(A[1] * A[2])%10] += 1

for i in range(2, N):
    for k in range(10):
        # F operation
        dp[i+1][(k+A[i+1])%10] += dp[i][k]
        dp[i+1][(k+A[i+1])%10] %= 998244353
        # G operation
        dp[i+1][(k*A[i+1])%10] += dp[i][k]
        dp[i+1][(k*A[i+1])%10] %= 998244353
for n in dp[N]:
    print(n%998244353)