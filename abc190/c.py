# ボールの置き方は2**16=65536通りぐらいで、
# M個の条件を満たしているかどうかにO(M)かかるので、
# 全体で10^7ぐらいなので、間に合いそうな気がする

N, M = [int(s) for s in input().split()]
conditions = []
for _ in range(M):
    conditions.append([int(s) for s in input().split()])
K = int(input())
cd = []
for _ in range(K):
    cd.append([int(s) for s in input().split()])

ans = 0
for i in range(2**K):
    ball = set()
    cnt = 0
    for j in range(K):
        if i >> j & 1:
            ball.add(cd[j][1])
        else:
            ball.add(cd[j][0])
    #print(ball)
    for c in conditions:
        if c[0] in ball and c[1] in ball:
            cnt += 1
    ans = max(ans, cnt)

print(ans)