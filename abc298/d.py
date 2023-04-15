## 普通に実装すると桁数がデカすぎて時間切れ
# Sのmod 998244353をTとおく
# 1のクエリは Sを10倍してxを加えるので
# T = T*10 + x (mod P)
# 2のクエリはSの最高桁をr、桁数をkとおくと r*10^kのmod Pをわかりたい
# kはたかだか6*10^5+1なので事前に計算しておけばいい(MLEしない)
# このMAPをM[k]とおくと
# T = T-r*M[k] mod P
from collections import deque
P = 998244353
S = deque([1])
Q = int(input())
mod_s = 1

# 10^kのmodを調べる
mod_map = {}
mod_map[1] = 10
for k in range(1, Q+1):
    mod_map[k+1] = (mod_map[k] * 10) % P

for _ in range(Q):
    query = [int(s) for s in input().split()]
    if query[0] == 1:
        x = query[1]
        #S += str(x)
        S.append(x)
        mod_s = (mod_s * 10 + x) % P
    elif query[0] == 2:
        r = S.popleft() # 最高桁
        k = len(S) # 桁数
        mod_s = (mod_s - r*mod_map[k]) % P
    else:
        print(mod_s)
        #print(int(S) % 998244353)