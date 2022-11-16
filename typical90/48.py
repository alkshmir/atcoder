N, K = [int(s) for s in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)

C = [a-b for a, b in zip(A, B)]
p = sorted(B + C, reverse=True)
print(sum(p[:K]))