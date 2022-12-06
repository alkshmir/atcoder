H, W = [int(s) for s in input().split()]
S = []
for _ in range(H):
    S.append(input())

cnt = 0
for s in S:
    for c in s:
        if c == '#':
            cnt += 1
print(cnt)