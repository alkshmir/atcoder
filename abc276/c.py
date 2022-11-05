from itertools import permutations
from collections import OrderedDict
from bisect import bisect_left

N = int(input())
P = [int(s) for s in input().split()]
P = tuple(P)

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i

#print(P)
all = list(permutations(list(range(1, N+1))))
#print(len(all))
'''
for i, p in enumerate(all):
    if p == P:
        #print(i)
        break
'''
i = index(all, P)
print(' '.join([str(n) for n in all[i-1]]))
