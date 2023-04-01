import math
from collections import defaultdict

def min_insuu(x):
    n = 1
    ans = x
    while n*n <= x:
        if x % n == 0:
            ans = min(ans, max(n, x//n))
        n += 1
    #print(ans)
    return ans
N, M = [int(s) for s in input().split()]

if N**2 < M:
    print(-1)
    exit()
if N >= M:
    print(M)
    exit()

# Mが合成すうの時、約数を最も小さくできる組み合わせを求めればいい

ans = min_insuu(M)
for i in range(M, N**2+1):
    tmp = min_insuu(i)
    if tmp <= N:
        print(i)
        exit()
print(-1)