from collections import defaultdict
N = int(input())
A = [int(s)%46 for s in input().split()]
B = [int(s)%46 for s in input().split()]
C = [int(s)%46 for s in input().split()]

a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)
for i in range(N):
    a[A[i]] += 1
for i in range(N):
    b[B[i]] += 1
for i in range(N):
    c[C[i]] += 1

cnt = 0
for x in range(46):
    for y in range(46):
        for z in range(46):
            if (x + y + z) % 46 == 0:
                cnt += a[x] * b[y] * c[z]
print(cnt)