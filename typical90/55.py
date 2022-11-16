import itertools
N, P, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

cnt = 0
for a in itertools.combinations(A, 5):
    tmp = 1
    for t in a:
        tmp *= t
    if tmp % P == Q:
        cnt += 1
print(cnt)