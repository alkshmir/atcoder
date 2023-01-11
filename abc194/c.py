# 展開するとAiだけの項とAjをj=1,...,i-1まで足した項とAj**2をj=1,...,i-1まで足した項が出てくる
# Aiだけの項はO(N)で求められ、後の2つは累積和に他ならずO(N)で事前に計算しておける
# よってO(N)で求められた
N = int(input())
A = [None] + [int(s) for s in input().split()]
cul_sum = [None, A[1]]
for a in A[2:]:
    cul_sum.append(a + cul_sum[-1])
cul_sum_square = [None, A[1]**2]
for a in A[2:]:
    cul_sum_square.append(a**2 + cul_sum_square[-1])

ans = 0
for i in range(2, N+1):
    ans += A[i]**2 * (i-1)

for i in range(2, N+1):
    ans += -2 * A[i] * cul_sum[i-1]

for i in range(2, N+1):
    ans += cul_sum_square[i-1]

print(ans)