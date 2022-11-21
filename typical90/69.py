N, K = [int(s) for s in input().split()]

def power(x, n, m):
    if n == 0: return 1
    if n % 2 == 0:
        return (power(x, n//2, m) **2)% m
    else:
        return (x * power(x,n-1,m)) % m

if N == 1:
    print(K % (10**9+7))
else:
    print((power(K-2,N-2,10**9+7) * K * (K-1))%(10**9+7) )