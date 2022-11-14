N, Q = [int(s) for s in input().split()]
X = []
for _ in range(Q):
    X.append(int(input()))

balls = {}
loc = {}
for i in range(1, N+1):
    balls[i] = i
    loc[i] = i

for x in X:
    if loc[x] != N:
        right = (loc[x] + 1)
        tmp = balls[right]
        balls[right] = balls[loc[x]]
        balls[loc[x]] = tmp
        loc[x] += 1
        loc[tmp] -= 1
    else:
        tmp = balls[N-1]
        balls[N-1] = balls[N]
        balls[N] = tmp
        loc[x] -= 1
        loc[tmp] += 1

print(' '.join([str(balls[i]) for i in range(1, N+1)]))