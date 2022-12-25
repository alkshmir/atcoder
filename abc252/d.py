import math
from collections import defaultdict
def combinations(n, k):
    if n < k: return 0
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
N = int(input())
A = [int(s) for s in input().split()]

dup = defaultdict(int)
for a in A:
    dup[a] += 1
tmp = 0
for k, v in dup.items():
    tmp += combinations(v, 2) * (N-v) + combinations(v, 3)
print(combinations(N, 3) - tmp)