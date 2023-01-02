# A_1の左には数がA_1-1こある
# A_i とA_i+1の間には数がA_i+1 - A_i - 1個ある
# A_Nの右には10^18 - A_N - 1こある
# このようにして作った要素数N+1の数列の累積和を取りS_iとおくと、
# S_i番目からS_i+1番目の値はA_iとA_i+1の間にある
# 従ってK_iをS内で二分探索して左側のSの要素をS_jとおき、これに対応するAの要素をA_jとおくと
# 求める値はA_j + (K_i - S_j)である
import bisect

N, Q = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
# A_i より小さくAに含まれない数の個数
S = [A[0]-1]
for i in range(N-1):
    S.append(A[i+1] - A[i] - 1 + S[-1])

#print(S)
for _ in range(Q):
    k = int(input())
    idx = bisect.bisect_left(S, k)
    #print("idx ", idx)
    if idx != 0:
        print(A[idx-1] + (k - S[idx-1]))
    else:
        print(k)