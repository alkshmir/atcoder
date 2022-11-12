import math

T = int(input())
L, X, Y = [int(s) for s in input().split()]
Q = int(input())
E = []
for _ in range(Q):
    E.append(int(input()))

for e in E:
    y = -L/2 * math.sin(2*math.pi/T*e)
    z = L/2 - L/2 * math.cos(2*math.pi/T*e)
    deg = math.degrees(math.atan2(z, math.sqrt(X**2+(Y-y)**2)))
    print(deg)