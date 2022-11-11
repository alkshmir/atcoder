import bisect

N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())
B = []
for _ in range(Q):
    B.append(int(input()))

# 二分探索 O(logN) 
# Q人分で O(QlogN)

A = sorted(A)
for b in B:
    i = bisect.bisect_left(A, b)
    possible = []
    if i < N:
        possible = [abs(A[i]-b)]
    if i > 0:
        possible.append(abs(A[i-1]-b))

    dissat = min(possible)


    print(dissat)