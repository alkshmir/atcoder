# Ai - x がAjとなるようなjがi<jであれば良い
# 値 -> 位置の最大値のmapを用意して、Ai - xが存在して、位置がiより大きければYes

N, X = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

s = set()
for a in A:
    s.add(a - X)
for a in A:
    if a in s:
        print("Yes")
        exit()
print("No")