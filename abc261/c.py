from collections import defaultdict
N = int(input())
S = []
for _ in range(N):
    S.append(input())

dic = defaultdict(int)
for i, s in enumerate(S):
    if dic[s] == 0:
        print(s)
    else:
        print(s+'('+str(dic[s])+')')
    dic[s] += 1
    
#print(dic)