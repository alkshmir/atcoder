# i個目の整数まで考えたとき、c_iがj以下となるような数列の個数をdp[i][j]とおく
# 求める数はdp[N][3000]
N = int(input())
A = [None] + [int(s) for s in input().split()]
B = [None] + [int(s) for s in input().split()]
c_max = 3000
dp = [[0 for _ in range(c_max+1)] for _ in range(N+1)]
for j in range(c_max+1):
    dp[1][j] += dp[1][j-1]
    if A[1] <= j <= B[1]:
        dp[1][j] += 1
#print(dp)
for i in range(1, N):
    for j in range(c_max+1):
        if A[i+1] <= j <= B[i+1]:
            dp[i+1][j] = dp[i][j] #* (j-A[i+1]+1)
            #dp[i+1][j] += 1
        dp[i+1][j] += dp[i+1][j-1] # j==0の時は変わらない
        dp[i+1][j] %= 998244353
        
#print(dp)
print(dp[N][c_max])