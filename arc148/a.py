import numpy as np
N = int(input())
A = [int(s) for s in input().split()]
k = []
for i in range(N-1):
    k.append(A[i+1] - A[i])

g = np.gcd.reduce(k)
if g != 1:
    print(1)
else:
    print(2)