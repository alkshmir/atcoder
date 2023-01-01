# X, Y座標それぞれに対して、重複を取り除いてソートした配列を作り、各要素がその配列のなかで何番目の値となるかを調べる
# O(NlogN)
import bisect
H, W, N = [int(s) for s in input().split()]
A = []
B = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)

sorted_A = sorted(set(A))
sorted_B = sorted(set(B))

for i in range(N):
    x = bisect.bisect_left(sorted_A, A[i])
    y = bisect.bisect_left(sorted_B, B[i])
    print(x+1, y+1)
# *3***
# 4***2
# *1***
# *****
# ↓
# *3*
# 4*2
# *1*