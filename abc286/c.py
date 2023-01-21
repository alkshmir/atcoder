# とけんかった
import math
N, A, B = [int(s) for s in input().split()]
S = input()

ans = math.inf
for i in range(N):
    rotated = S[i:N] + S[:i]
    cost = i * A
    for j in range(N//2):
        if rotated[j] != rotated[N-1-j]:
            cost += B
    #print(cost)
    ans = min(ans, cost)
print(ans)