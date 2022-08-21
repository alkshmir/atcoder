N, M, T = [int(s) for s in input().split()]
A = [0] + [int(s) for s in input().split()]
XY = {}
for _ in range(M):
    x, y = [int(s) for s in input().split()]
    XY[x] = y

t = T
#print(XY)
for i in range(1, N):
    if i in XY:
        t += XY[i]
    t -= A[i]
    if t <= 0:
        print("No")
        exit()
    #print(t)
print("Yes")