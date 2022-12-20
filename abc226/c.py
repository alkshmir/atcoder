N = int(input())
T = []
A = []
for _ in range(N):
    tmp = [int(s) for s in input().split()]
    T.append(tmp[0])
    k = tmp[1]
    A.append(tmp[2:])

todo = [False for _ in range(N)]
todo[-1] = True
ans = 0
for i in range(N-1, -1, -1):
    if not todo[i]:
        continue
    ans += T[i]
    for j in A[i]:
        todo[j-1] = True
print(ans)

#for i in range(N-1, -1, -1):
#    A[i]