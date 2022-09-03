from cmath import inf
import itertools
N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

accum = [0] + list(itertools.accumulate(A))

iai = 0
for i in range(1, M+1):
    iai += i * A[i-1]

ibi = []
ibi.append(iai)
for i in range(1, N-M+1):
    ibi.append( ibi[-1] + M*A[M+i-1] - (accum[M+i-1] - accum[i-1]))
    
print(max(ibi))