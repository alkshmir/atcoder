N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

for _ in range(K):
    A = A[1:] + [0]
print(' '.join([str(n) for n in A]))