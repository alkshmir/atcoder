N = int(input())
A = [int(s) for s in input().split()]
called = [False for _ in range(N)]

for i in range(N):
    if not called[i]:
        called[A[i]-1] = True
#print(called)
ans = []
for i in range(N):
    if not called[i]:
        ans.append(str(i+1))

print(len(ans))
print(" ".join(ans))