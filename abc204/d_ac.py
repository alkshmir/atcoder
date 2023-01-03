import math
N = int(input())
T = [int(s) for s in input().split()]
sumT = sum(T)
T = [None] + T
# dp[i][j]をi番目までの数を使って部分和をjにすることができるかを表す真偽値とする
dp = [[False for _ in range(sumT+1)] for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for j in range(sumT+1):
        if j >= T[i+1]:
            dp[i+1][j] = dp[i][j-T[i+1]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

for j in range(math.ceil(sumT/2), sumT+1):
    if dp[N][j]:
        print(j)
        break