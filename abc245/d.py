N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
C = [int(s) for s in input().split()]
B = [None for _ in range(M+1)]


for n in range(M, -1, -1):
    tmp = 0
    for i in range(M, n, -1):
        j = n-i+N
        if j>N or j<0:
            continue
        #print(i, j)
        tmp += A[j] * B[i]
    B[n] = (C[n+N] - tmp) // A[N]

print(' '.join([str(i) for i in B]))