N = int(input())
T = []
TXA = {}
for _ in range(N):
    t, x, a = [int(s) for s in input().split()]
    TXA[t] = (x, a)
    T.append(t)
    #X.append(x)
    #A.append(a)

dp = [[0 for _ in range(5)] for _ in range(T[-1]+1)]

for t in range(1, T[-1]+1):
    for x in range(5):
        if t in TXA and TXA[t][0] == x:
            bonus = TXA[t][1]
        else:
            bonus = 0
        dp[t][x] = max(dp[t-1][max(x-1, 0)], dp[t-1][x], dp[t-1][min(x+1, 4)]) + bonus
    if t == 1:
        dp[t][2] = 0
        dp[t][3] = 0
        dp[t][4] = 0
    elif t == 2:
        dp[t][3] = 0
        dp[t][4] = 0
    elif t == 3:
        dp[t][4] = 0

print(max(dp[-1]))