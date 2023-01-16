# 9をNこ並べた数字、8をN個並べた数字,..., 1をNこ並べた数字、
# 9をN-1個並べた数字、のように数えていくとN*9回ぐらい数えれば良い
# N<= 10**5なので間に合う…と思いきや、デカすぎる数字どうしの割り算が遅いのでTLE

N, M = [int(s) for s in input().split()]

x = [[0 for _ in range(10)] for _ in range(N+1)]
ans = 0
for i in range(1, N+1):
    for j in range(1, 10):
        x[i][j] = 10*x[i-1][j] + j
        x[i][j] %= M
        if x[i][j] == 0:
            ans = max(ans, i)

if ans == 0:
    print(-1)
    exit()
for j in range(9, 0, -1):
    if x[ans][j] == 0:
        print(str(j)*ans)
        break
