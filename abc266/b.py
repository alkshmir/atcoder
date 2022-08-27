import math 

N = int(input())


k = math.floor(N/998244353)

print(N-k*998244353)