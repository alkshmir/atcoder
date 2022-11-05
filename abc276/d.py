import numpy as np

N = int(input())
a = [int(s) for s in input().split()]
g = np.gcd.reduce(a)

ans = 0
for n in a:
    n /= g
    while(n%2 == 0):
        n /= 2
        ans += 1
    while(n%3 == 0):
        n /= 3
        ans += 1
    if n != 1:
        print(-1)
        exit()
print(ans)