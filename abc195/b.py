
a, b, w = [int(s) for s in input().split()]

ma = 0
mi = 10**6+1
for n in range(1, 10**6+1):
    if a*n <= 1000*w <= b*n:
        ma = max(ma, n)
        mi = min(mi, n)
if ma == 0:
    print("UNSATISFIABLE")
else:
    print(mi, ma)