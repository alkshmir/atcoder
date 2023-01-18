# Aの要素から2つ選ぶ全ての組み合わせについて差の絶対値をとり合計するので、
# 足す順番は任意に変えて良い
# よって、例えば降順にソートすれば絶対値がそのまま外れてiとjごとに計算できる
# 計算量はソートがボトルネックでありO(NlogN)

N = int(input())
A = [int(s) for s in input().split()]
A.sort(reverse=True)
A = [None] + A

cul_sum = [None, A[1]]
for i in range(2, N+1):
    cul_sum.append(cul_sum[-1] + A[i])
#print(A)
#print(cul_sum)
ans = 0
for i in range(1, N):
    ans += (N-i)*A[i]
for i in range(1, N):
    ans -= cul_sum[N] - cul_sum[i]
print(ans)