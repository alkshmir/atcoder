from collections import defaultdict
import bisect
N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())

at = defaultdict(list)
for i, a in enumerate(A):
    at[a].append(i)

for _ in range(Q):
    l, r, x = [int(s) for s in input().split()]
    print(bisect.bisect_right(at[x], r-1) - bisect.bisect_left(at[x], l-1))