import numpy as np

N = int(input())
S = input()
S = np.array([True if s == '1' else False for s in S])
W = [int(s) for s in input().split()]

def f(x):
    # O(n)
    est = np.array([True if w >= x else False for w in W])
    return np.sum(~(est ^ S))

sorted_w = np.sort(W)
#print(sorted_w)
est = []
# O(n^2)なので非常に遅い
for n in range(N+1):
    if n == 0:
        x = W[0] - 1
    elif n == N:
        x = W[-1] + 1
    else:
        x = W[n] + 0.1
    est.append(f(x))

print(max(est))