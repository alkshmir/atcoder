N, X, Y = [int(s) for s in input().split()]

r = [0]
b = [0]
r.append(0) # level 1の赤からは0個
b.append(1) # level 1の青から1個

for i in range(1, N):
    #print(i, b, r)
    b.append(r[-1] + Y * b[-1])
    r.append(r[-1] + X * b[-1])
print(r[-1])