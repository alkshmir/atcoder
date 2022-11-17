from queue import deque

yamahuda = deque()
Q = int(input())
T = []
X = []
for _ in range(Q):
    t, x = [int(s) for s in input().split()]
    T.append(t)
    X.append(x)

for t, x in zip(T, X):
    if t == 1:
        yamahuda.appendleft(x)
    elif t == 2:
        yamahuda.append(x)
    elif t == 3:
        print(yamahuda[x-1])