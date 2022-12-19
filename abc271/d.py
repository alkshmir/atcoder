N, S = [int(s) for s in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)

# i番目までのカードで総和をjにすることができるかどうか dp[i][j]
dp = [[0 for _ in range(100*100+1)] for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(100*100+1):
        if dp[i][j]:
            dp[i+1][j+A[i]] = 1
            dp[i+1][j+B[i]] = 2
#print(dp[N][S])
if dp[N][S]:
    print("Yes")
else:
    print("No")
    exit()
s = S
ans = []
for n in range(N, 0, -1):
    if dp[n][s] == 1:
        ans.append('H')
        s -= A[n-1]
    elif dp[n][s] == 2:
        ans.append('T')
        s -= B[n-1]
print(''.join(ans[::-1]))