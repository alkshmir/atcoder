
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]
C = [int(s) for s in input().split()]
D = [int(s) for s in input().split()]

def outerProduct(p1, p2, p3):
    return (p1[0]-p3[0]) * (p2[1]-p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1]) 
def isPointInTriangle(p, v1, v2, v3):
    b1 = outerProduct(p, v1, v2) < 0
    b2 = outerProduct(p, v2, v3) < 0
    b3 = outerProduct(p, v3, v1) < 0
    return ((b1==b2) and (b2==b3))

# abc
d = isPointInTriangle(D, A, B, C)
# bcd
a = isPointInTriangle(A, B, C, D)
# dab
c = isPointInTriangle(C, D, A, B)
# acd
b = isPointInTriangle(B, A, C, D)

if a or b or c or d:
    print("No")
else:
    print("Yes")


'''
# 3点から角度を求める
def getAngle(d, a, b):
    if abs(a[1] - b[1]) == 0:
        return math.atan(abs(a[0]-d[0])/abs(a[1]-d[1]))
    elif abs(a[1] - d[1]) == 0:
        return math.atan(abs(a[0]-b[0])/abs(a[1]-b[1]))
    else:
        return math.atan(abs(a[0]-b[0])/abs(a[1]-b[1])) + math.atan(abs(a[0]-d[0])/abs(a[1]-d[1]))

dab = getAngle(D, A, B)
abc = getAngle(A, B, C)
bcd = getAngle(B, C, D)
cda = getAngle(C, D, A)
'''
