from collections import defaultdict
#素因数分解して各素数の肩についている数の合計を2でわればよい

N = int(input())

primes = defaultdict(int) #含まれる素数と多重度
i = 2
while(i*i <= N):
    while(N % i == 0):
        primes[i] += 1
        N = N // i
    i += 1
if N != 1:
    primes[N] += 1
    #print(i, N)
#print(primes)
ans = 0
s = sum([v for v in primes.values()])
while(2**ans < s):
    ans += 1
print(ans)