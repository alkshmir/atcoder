# Nを素因数分解するとO(N^(1/2))でありまにあわない
# Nの1/3乗以下の素数はO(N^(1/3))で列挙できる
# 10^6個ぐらいある
import math
from collections import defaultdict

def factorize(n):
    div = defaultdict(int)
    while(n%2 == 0):
        div[2] += 1
        n //= 2
    f = 3
    while (f*f*f <= n):
        if (n%f == 0):
            div[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        div[n] += 1
    return div
def sqrt(n):
    if n == 4:
        return 2
    i = 3
    while i*i < n:
        i += 2
    if i*i == n:
        return i
    
T = int(input())
for _ in range(T):
    N = int(input())
    div = factorize(N)
    #print(div)
    if 2 in div.values():
        for k, v in div.items():
            if v == 2:
                p = k
            else:
                q = k
        print(p, q)
        continue
    pq = div.keys()
    if max(pq) % min(pq) == 0:
        p = min(pq)
        q = max(pq)//p
        print(p, q)
    else:
        print(math.isqrt(max(pq)), min(pq))