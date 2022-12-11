#from collections import defaultdict
# そもそも間違っている(WAは出なかったけど)
# あるマスxのhop数がpだった時に、iがp+1より大きければ、xからa[i]またはb[i]で移動することはできない。
# 2つ以上前のhopからa[i]またはb[i]を使って移動することはできない。
# 次の移動を考えるときは、1つ前のhopからa[i]またはb[i]で移動する場合のみを考えればよく、逆にそれ以外の移動はできない。

N, X = [int(s) for s in input().split()]
#n_hop = defaultdict(list)
n_hop = [[] for _ in range(X+1)]
A = []
B = []
for i in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)
n_hop[0].append(0)
for i in range(X):
    if n_hop[i] == []:
        continue
    for hop in n_hop[i]:
        if hop >= N:
            continue
        if i+A[hop] <= X:
            n_hop[i+A[hop]].append(hop+1)
        if i+B[hop] <= X:
            n_hop[i+B[hop]].append(hop+1)
    #print(n_hop)
print(n_hop)
if N in n_hop[X]:
    print("Yes")
else:
    print("No")