from cmath import inf


N, W = [int(s) for s in input().split()]
weights = [0]
values = [0]
for _ in range(N):
    w, v = [int(s) for s in input().split()]
    weights.append(w)
    values.append(v)

v_max = 100000

dp = [[inf for _ in range(v_max+1)] for _ in range(N+1)]
dp[1] = [inf] + [weights[1] if values[1] == j else inf for j in range(1, v_max+1)]
#dp[0][0] = 0
for i in range(1, N):
    dp[i+1] = [inf] + [min(dp[i][j - values[i+1]]+weights[i+1], dp[i][j]) if values[i+1] <= j 
                    else dp[i][j] for j in range(1, v_max+1)]
    #print(dp)
for j in range(v_max, -1, -1):
    #if j % 100 == 0:
    #    print(j, dp[N][j])
    if dp[N][j] <= W:
        print(j)
        break
#print(dp[-1][-1])
