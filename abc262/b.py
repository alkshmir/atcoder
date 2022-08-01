N, M = [int(s) for s in input().split()]
UV = set()
for _ in range(M):
    u, v = [int(s) for s in input().split()]
    UV.add((u,v))

cnt = 0
for c in range(3, N+1):
    for b in range(2, c):
        for a in range(1, b):
            if (a, b) in UV and (b, c) in UV and (a, c) in UV:
                cnt += 1

print(cnt)