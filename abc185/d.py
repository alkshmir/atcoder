# Aをソートして、
# Aの要素の差(及びA_1-1, N-A_M)のうち1でないものの最小値
# を求めればそれがkである
# あとはさっき求めたAの要素の差をD_iとするとceil(D_i/k)を足していけば答えである
# 計算量はソートがボトルネックでO(MlogM)
import math
N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
A.sort()

if N == M:
    print(0)
    exit()
if M == 0:
    print(1)
    exit()

D = [A[0]-1]
for i in range(1, M):
    D.append(A[i]-A[i-1]-1)
D.append(N-A[-1])
#print(A)
#print(D)
k = N
for d in D:
    if d >= 1:
        k = min(k, d)

ans = 0
for d in D:
    if d >= 1:
        ans += math.ceil(d/k)
print(ans)