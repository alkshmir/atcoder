
from collections import defaultdict
import numpy as np
def inv_argsort(array_input):
    return np.argsort(np.argsort(array_input))

N = int(input())
A = [int(s) for s in input().split()]

#argsort_A = np.argsort(A )
#print(sorted(A))
#print(inv_argsort(A))
#print(argsort_A)
setA = set(A)
#print(list(setA))
ranking_mapping = inv_argsort(list(setA))

dic = {}
for i, key in enumerate(list(setA)):
    dic[key] = len(setA) - ranking_mapping[i] - 1

# 多重度
multip = defaultdict(int)
for a in A:
    multip[a] += 1

#print(dic)
inv_dic = defaultdict(int)
for k, v in dic.items():
    inv_dic[v] += multip[k]

#print(inv_dic)

#print(multip)
#print(ranking_mapping)
# dic のvalがKであるようなitemはAに何個含まれるかをしらべればよい
for K in range(N):
    print(inv_dic[K])