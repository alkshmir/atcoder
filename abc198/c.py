# 原点と(X, Y)との距離をRで割ったときの値を切り上げれば答え
import math
R, X, Y = [int(s) for s in input().split()]
d = math.sqrt(X**2+Y**2)
if d < R:
    print(2)
else:
    print(math.ceil(d/R))
