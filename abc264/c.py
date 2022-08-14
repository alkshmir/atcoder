from itertools import combinations
import numpy as np

h1, w1 = [int(s) for s in input().split()]
A = np.array([[int(s) for s in input().split()] for _ in range(h1)])
h2, w2 = [int(s) for s in input().split()]
B = np.array([[int(s) for s in input().split()] for _ in range(h2)])

hw = [0 for _ in range(h1+w1)]

yes = False
for hi in combinations(range(h1), h2):
    for wi in combinations(range(w1), w2):
        if np.all(A[hi,:][:,wi] == B):
            yes = True
            break

if yes:
    print("Yes")
else:
    print("No")
            