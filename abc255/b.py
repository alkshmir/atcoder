import math

def euc_dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2) 

N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
X = []
Y = []
for _ in range(N):
    x, y = [int(s) for s in input().split()]
    X.append(x)
    Y.append(y)

nearest_light = []
for i in range(N):
    nearest_light.append(min([euc_dist(X[a-1], Y[a-1], X[i], Y[i]) for a in A]))
#print(nearest_light)
print(max(nearest_light))