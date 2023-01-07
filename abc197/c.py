# AをN-1個以下の仕切りで区切ることを考えると
# 区切り方の総数は2^(N-1)通りである
# 区切り方が決まればN回の演算で計算できるので
# 10^7くらいの演算回数で求められる
import math

N = int(input())
A = [int(s) for s in input().split()]
ans = math.inf

for i in range(2**(N-1)):
    stack = []
    stack.append(A[0])
    for j in range(N-1):
        if i >> j & 1:
            stack.append(A[j+1])
        else:
            stack[-1] |= A[j+1]
    
    tmp = stack[0]
    for a in stack[1:]:
        tmp ^= a
    ans = min(ans, tmp)
print(ans)
