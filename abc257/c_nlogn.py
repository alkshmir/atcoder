import numpy as np

N = int(input())
S = np.array([int(s) for s in input()])
#S = np.array([True if s == '1' else False for s in S])
W = np.array([int(s) for s in input().split()])

def f(x):
    # O(n)
    est = np.array([True if w >= x else False for w in W])
    return np.sum(~(est ^ S))

def sort_on_raw(a_2d, row_num):
    return a_2d[:, np.argsort(a_2d[row_num])]

# weight and flag
ws = sort_on_raw(np.stack([W,S]), 0)

fx = np.sum(S) # 大人の数
ans = fx
for n in range(N):
    if ws[1][n] == 1: #大人
        fx -= 1
    else:
        fx += 1
    if n < N-1:
        if ws[0][n] != ws[0][n+1]:
            ans = max(ans, fx) #次の値が異なるときだけ増やす
    else:
        ans = max(ans, fx)

print(ans)