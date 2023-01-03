# 料理iまでを料理するのにかかる時間が最短となるとき、
# オーブンj (={0, 1})での調理時間をdp[i][j]とおく。
# ただしdp[0][0] >= dp[0][1]となるように選ぶとする。

N = int(input())
T = [int(s) for s in input().split()]
T.sort(reverse=True)
dp = [[10**5 for _ in range(2)] for _ in range(N)]
dp[0][0] = T[0]
dp[0][1] = 0

for i in range(1, N):
    t = T[i]
    # オーブン0で焼く方が早い場合
    if max(dp[i-1][0] + t, dp[i-1][1]) <= max(dp[i-1][0], dp[i-1][1] + t):
        dp[i][0] = dp[i-1][0] + t 
        dp[i][1] = dp[i-1][1]
    else:
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1] + t
print(max(dp[-1][0], dp[-1][1]))