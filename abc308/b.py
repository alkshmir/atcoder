N, M = [int(s) for s in input().split()]
C = [s for s in input().split()]
D = [s for s in input().split()]
P = [int(s) for s in input().split()]

from collections import defaultdict
price = defaultdict(lambda: P[0])
for d, p in zip(D, P[1:]):
    price[d] = p

eaten = 0
for c in C:
    eaten += price[c]
print(eaten)