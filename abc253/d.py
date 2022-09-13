import math
def lcm(a, b):
    return a * b // math.gcd(a, b)

N, A, B = [int(s) for s in input().split()]

ans = N*(N+1)//2
n = N//A
#if n > 0:
ans -= A*n*(n+1)//2
n = N//B
#f n > 0:
ans -= B*n*(n+1)//2
L = lcm(A, B)
n = N//L
#if n > 0:
ans += L*n*(n+1)//2

print(int(ans))