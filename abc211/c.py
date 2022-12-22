S = input()
T = "chokudai"
dp = [[None for _ in range(9)] for _ in range(len(S)+1)]
for i in range(1, 9):
    dp[0][i] = 0
for i in range(len(S)+1):
    dp[i][0] = 1

for i in range(1, len(S)+1):
    for j in range(1,9):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1] % (10**9+7))
