import math

N, M = [int(s) for s in input().split()]

ans = math.inf

for a in range(1, N+1):
    b = math.ceil(M/a)
    if b <= N:
        ans = min(ans, a*b)
    if a > b:
        break
if ans == math.inf:
    print(-1)
else:
    print(ans)
