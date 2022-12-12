# CからDの任意の整数yについて、x+yが素数とならないようにxをAからBの範囲で選べるか？
import math
def sieve_of_eratosthenes(n):
    ceil = math.ceil(math.pow(n, 1/2)) +1
    #print(ceil)
    prime = [True for _ in range(n+1)]
    prime[0] = False
    prime[1] = False

    for i in range(2, ceil+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    ans = []
    for i, p in enumerate(prime):
        if p:
            ans.append(i)
    return ans

A, B, C, D = [int(s) for s in input().split()]
primes = sieve_of_eratosthenes(200)


for x in range(A, B+1):
    flag = True
    for y in range(C, D+1):
        if x+y in primes:
            flag = False
            break
    if flag:
        print("Takahashi")
        exit()
print("Aoki")
    