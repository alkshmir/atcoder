N = int(input())
A = []
for _ in range(N):
    A.append([int(s) for s in input().split()])

s = [sum(a) for a in A]
ans = 1
for p in s:
    ans *= p
print(ans%(10**9+7))