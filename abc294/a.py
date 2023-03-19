N = int(input())
A = [int(s) for s in input().split()]
ans = []
for a in A:
    if a % 2 == 0:
        ans.append(str(a))
print(' '.join(ans))