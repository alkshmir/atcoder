# pypy7.3.0 だとmath.combがないので注意
# math.combがない場合はmath.factorialで代用する
# def combinations_count(n, k):
#    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
from collections import defaultdict
import math
N = int(input())
S = []
for _ in range(N):
    S.append(input())

charset = defaultdict(int)
for s in S:
    l = [0 for _ in range(26)]
    for c in s:
        l[ord(c)-97] += 1
    charset[tuple(l)] += 1
cnt = 0
for k, v in charset.items():
    if v >= 2:
        cnt += math.comb(v, 2)
print(cnt)