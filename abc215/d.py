# Aiに出てくる素因数の積lを計算し、各kでgcdが1かどうかを調べれば、
# O(N*max(A_i)^(1/2)+M)で間に合いそうだが、
# lが非常に大きくなるのでTLEする。
# C++などに書き換えた場合、lが64bitに収まらないのでWAになる。
# よく考えると、Aに含まれる素数が5桁だとするとlは10^(5*10^5)程度になり、クソでかい。
# そこで、Aに含まれる素数は10000個程度なので、kを割りきれるかどうかを調べれば間に合う。
# x以下の素数の個数をπ(x)と書くと、計算量はO(N*max(A_i)^(1/2)+Mπ(max(A_i))
# こう書くとMπ(max(A_i)の部分がギリギリに見えるが、C++はとても速いので間に合う
# (あと割りきれるかどうかを調べるだけならはやい)。
# 解説にあるように、エラストテネスの篩を利用して既に確認した因数を持つ候補を消していく
# 方がスマートでしょう…
import math
#from collections import defaultdict

N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
primes = set()
def prime_factorize(n):
    primes.add(1)
    while n % 2 == 0:
        primes.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            primes.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        primes.add(n)
    return a


for a in A:
    prime_factorize(a)

l = primes.pop()
while len(primes):
    l *= primes.pop()
ans = []
for k in range(1, M+1):
    if math.gcd(l, k) == 1:
        ans.append(k)
print(len(ans))
for a in ans:
    print(a)   

'''
import functools
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)
lcm = my_lcm(*A)
#print(lcm)
ans = []
for k in range(1, M+1):
    if math.gcd(lcm, k) == 1:
        ans.append(k)
print(len(ans))
for a in ans:
    print(a)        
'''


