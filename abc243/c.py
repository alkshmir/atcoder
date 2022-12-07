from collections import defaultdict
import math
N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = [int(s) for s in input().split()]
    X.append(x)
    Y.append(y)
S = input()

max_x_l = defaultdict(lambda: 0)
min_x_r = defaultdict(lambda: 10**9)

for x, y, s in zip(X, Y, S):
    if s == 'L':
        max_x_l[y] = max(max_x_l[y], x)
    else:
        min_x_r[y] = min(min_x_r[y], x)
#print(max_x_l, min_x_r)
for y in Y:
    if max_x_l[y] > min_x_r[y]:
        print("Yes")
        exit()
print("No")