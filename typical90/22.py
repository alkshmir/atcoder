import numpy as np
A, B, C = [int(s) for s in input().split()]

g = np.gcd.reduce([A, B, C])

print(A//g -1 + B//g -1 + C//g -1)