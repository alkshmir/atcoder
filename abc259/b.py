import math

def getRD(x, y):
    r = math.sqrt(x**2+y**2)
    rad = math.atan2(y, x)
    degree = math.degrees(rad)
    #print(r, degree)
    return r, degree

def getXY(r, degree):
    # 度をラジアンに変換
    rad = math.radians(degree)
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    #print(x, y)
    return x, y

inp = [int(i) for i in input().split()]
a = inp[0]
b = inp[1]
d = inp[2]

r, degree = getRD(a, b)
degree += d

a_new, b_new = getXY(r, degree)
print(a_new, b_new)