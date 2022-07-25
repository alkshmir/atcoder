N, W = [int(s) for s in input().split()]
weights = [0]
values = [0]
for _ in range(N):
    w, v = [int(s) for s in input().split()]
    weights.append(w)
    values.append(v)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

dp[1] = [0] + [values[1] if weights[1] <= j else 0 for j in range(1, W+1)]
for i in range(1, N):
    dp[i+1] = [0] + [max(dp[i][j - weights[i+1]]+values[i+1], dp[i][j]) if weights[i+1] <= j else dp[i][j] for j in range(1, W+1)]
    #print(dp)    
print(dp[-1][-1])
