from collections import defaultdict
import math
K = int(input())
K_orig = K

primes = defaultdict(int) #含まれる素数と多重度
i = 2
while(i*i <= K):
    while(K % i == 0):
        primes[i] += 1
        K = K // i
    i += 1
if K != 1:
    primes[K] += 1

print(primes)
n = 0
for k, v in primes.items():
    n = max(n, k*v)
print(n, math.factorial(n)/K_orig)
for i in range(1, n+1):
    print(i, math.factorial(i)/K_orig)