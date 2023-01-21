# 部分和問題と同じである
# 整数列の長さは50 * 50 = 2500
# dp[i][j]をi番目までの整数の中からいくつか選んで総和をjとすることが可能か
# 計算量はO(sum(B)*X)

N, X = [int(s) for s in input().split()]
coins = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    for _ in range(b):
        coins.append(a)

dp = [[False for _ in range(X+1)] for _ in range(len(coins)+1)]

dp[0][0] = True
for i in range(len(coins)):
    for j in range(X+1):
        if j-coins[i] >= 0 and dp[i][j-coins[i]]:
            dp[i+1][j] = True
        if dp[i][j]:
            dp[i+1][j] = True

if dp[-1][X]:
    print("Yes")
else:
    print("No")
