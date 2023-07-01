N = int(input())
A = [int(s) for s in input().split()]

s = 0
ans = []
for i in range(N):
    ans.append(str(sum(A[i*7:min((i+1)*7, len(A))])))
print(' '.join(ans))