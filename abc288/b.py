N, K = [int(s) for s in input().split()]
S = []
for _ in range(N):
    S.append(input())

for n in sorted(S[:K]):
    print(n)