# @を除いて差の集合をとる
# TにあってSにない要素が"atcoder"のいずれかであり、総数がSの@の数以下であればSはTをすべて含むことができる
# (逆に、その条件をみたせなければNo)
# SにあってTにない要素に対して同じことをして、条件を満たせればYesである。

from collections import defaultdict

S = input()
T = input()

S_at = S.count("@")
T_at = T.count("@")

S_multiset = defaultdict(int)
T_multiset = defaultdict(int)

for s in S:
    if s != '@':
        S_multiset[s] += 1
for t in T:
    if t != '@':
        T_multiset[t] += 1

# SにあってTにない要素
S_and_not_T = defaultdict(int)
S_and_not_T_total = 0
for k, v in S_multiset.items():
    n = v - T_multiset[k]
    if n > 0:
        S_and_not_T[k] = n
        S_and_not_T_total += int(n)
        if k not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:
            print("No")
            exit()
# TにあってSにない要素
T_and_not_S = defaultdict(int)
T_and_not_S_total = 0
for k, v in T_multiset.items():
    n = v - S_multiset[k]
    if n > 0:
        T_and_not_S[k] = n
        T_and_not_S_total += int(n)
        if k not in ['a', 't', 'c', 'o', 'd', 'e', 'r']:
            print("No")
            exit()
#print(S_and_not_T)
#print(T_and_not_S)

if S_and_not_T_total <= T_at and T_and_not_S_total <= S_at:
    print("Yes")
else:
    print("No")
