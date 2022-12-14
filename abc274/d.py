# 奇数ばんめは全てx座標に作用し、偶数番目はy座標に作用する
# よって、x座標を合わせられるかという問題とy座標を合わせられるかという問題に分けられる
# 本質的に同じ問題なので、以下ではx座標を合わせることだけを考える。
# O(N)個の符合の全組み合わせを考えるとO(2^N)になってしまうので到底間に合わない
# dp[i][j]をaをi番目まで使った時に、値をjにすることが可能か(bool)とする
# dp[1][j] = True if j = abs(a[1]) else False
# dp[i+1][j] = True if dp[i][j-a[i+1]] or dp[i][j+a[i+1]] else False
# iは1からNまで、jは-10*Nから10*Nまで考えれば良いのでO(|A|N^2)でx座標を合わせられるかを求められる
import math
N, x, y = [int(a) for a in input().split()]
A = [int(s) for s in input().split()]

#print(math.ceil(N/2), math.floor(N/2))
odds = [A[2*i] for i in range(1, math.ceil(N/2))]
even = [A[2*i+1] for i in range(math.floor(N/2))]

#print(odds, even)

def sign_sum(series, x):
    n = len(series)
    series = [0] + series
    dp = [[False for _ in range(-10*n+5, 10*n+5000)] for _ in range(n+1)]
    for j in range(-10*n-1, 10*n+1):
        if j in [series[1], -series[1]]:
            dp[1][j] = True
        #else:
        #    dp[1][j] = False
    for i in range(n):
        for j in range(-10*n-1, 10*n+1):
            minus = j - series[i+1]
            plus =  j + series[i+1]
            if -10*n <= minus <= 10*n and dp[i][minus] or -10*n <= plus <= 10*n and dp[i][plus]:
                dp[i+1][j] = True
    return dp[n][x]

#print(sign_sum(odds, x-A[0]), sign_sum(even, y))
if sign_sum(odds, x-A[0]) and sign_sum(even, y):
    print("Yes")
else:
    print("No")