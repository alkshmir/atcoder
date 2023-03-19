N, M = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]
C = A + B
C.sort()
ans_dic = {}
for i, c in enumerate(C):
    ans_dic[c] = i+1

#print(ans_dic)
print(' '.join([str(ans_dic[a]) for a in A]))
print(' '.join([str(ans_dic[b]) for b in B]))
