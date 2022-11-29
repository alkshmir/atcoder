from bisect import bisect_left
N, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
X = []
for _ in range(Q):
    X.append(int(input()))
A.sort()
cul_sum = [A[0]]
for i in range(1, N):
    cul_sum.append(cul_sum[-1]+A[i])
#print(A)
#print(cul_sum)
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    
for x in X:
    i = bisect_left(A, x)
    #print(x, i)
    if i != 0 and i != N:
        
        ans = abs(cul_sum[i-1]-i*x) + abs(cul_sum[-1]-cul_sum[i-1]-(N-i)*x)
    else:
        ans = abs(cul_sum[-1] - N*x)
    print(ans)