import math
N, X = [int(s) for s in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)
C = [a + b for a, b in zip(A, B)]
C_cul = [C[0]]
for i in range(1, N):
    C_cul.append(C[i] + C_cul[i-1])
ans = math.inf
for i in range(min(N,X)):
    ans = min(ans, C_cul[i] + (X-i-1)*B[i])

print(ans)