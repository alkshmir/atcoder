import bisect
N, T = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
cul = [A[0]]
for i in range(1, N):
    cul.append(cul[-1] + A[i])
#print(cul)
idx = bisect.bisect_left(cul, T%cul[-1])
if idx == 0:
    offset = 0
else:
    offset = cul[idx-1]
print(idx+1, T%cul[-1]-offset)
