
from collections import deque
N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

j = 0
stack = deque()
ans = []
for i in range(1, N+1):
    #print(j)
    if j < M and i == A[j]:
        stack.appendleft(i)
        j+=1
    else:
        stack.appendleft(i)
        #print(' '.join([str(i) for i in stack]), end=' ')
        ans += stack
        stack = deque()
print(' '.join([str(i) for i in ans]))
