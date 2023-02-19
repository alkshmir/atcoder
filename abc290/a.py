N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]

ans = 0
for b in B:
    ans += A[b-1]
print(ans)