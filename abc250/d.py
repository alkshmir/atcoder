import math
def sieve_of_eratosthenes(n):
    ceil = math.ceil(math.pow(n, 1/3)) +1
    #print(ceil)
    prime = [True for _ in range(ceil+1)]
    prime[0] = False
    prime[1] = False

    for i in range(2, ceil+1):
        if prime[i]:
            for j in range(2*i, ceil+1, i):
                prime[j] = False
    ans = []
    for i, p in enumerate(prime):
        if p:
            ans.append(i)
    return ans

N = int(input())

prime = sieve_of_eratosthenes(N)
#print(prime)
cnt = 0

l = 0
r = len(prime) - 1

while r > l:
    while prime[l] * prime[r]**3 > N and r>l:
        r -= 1
    cnt += r-l
    l += 1 

print(cnt)