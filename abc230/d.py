# 区間スケジューリング問題
from operator import itemgetter
N, D = [int(s) for s in input().split()]
LR = []
for _ in range(N):
    LR.append([int(s) for s in input().split()])
LR.sort(key=itemgetter(1))
x = LR[0][1]
cnt = 1
for i in range(1, N):
    l, r = LR[i]
    if l > x+D-1:
        x = r
        cnt += 1
print(cnt)
