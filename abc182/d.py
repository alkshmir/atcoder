# 累積和を考えると、今xにいるときk回目の移動における座標の最大値は、
# x+(kまでの累積和の最大値)
# である
N = int(input())
A = [int(s) for s in input().split()]

cul_sum = [A[0]]
for i in range(1, N):
    cul_sum.append(cul_sum[-1] + A[i])
cul_sum_max = [cul_sum[0]]
for i in range(1, N):
    cul_sum_max.append(max(cul_sum_max[-1], cul_sum[i]))

x = 0
max_x = 0
partial_sum = 0
for a, csm in zip(A, cul_sum_max):
    max_x = max(max_x, x + csm)
    partial_sum += a
    x += partial_sum

print(max_x)