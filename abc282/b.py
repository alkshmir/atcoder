import itertools
N, M = [int(s) for s in input().split()]
S = []
for _ in range(N):
    S.append(input())
cnt = 0
for (i, j) in itertools.combinations(range(N), 2):
    for k in range(M):
        success = True
        if S[i][k] == 'x' and S[j][k] == 'x':
            success = False
            break
    if success:
        cnt += 1
print(cnt)
