from collections import defaultdict
H, W = [int(s) for s in input().split()]
S = []
T = []
for _ in range(H):
    S.append([s for s in input()])

for _ in range(H):
    T.append([s for s in input()])

S_dic = defaultdict(int)
for j in range(W):
    S_dic[tuple([S[i][j] for i in range(H)])] += 1
T_dic = defaultdict(int)
for j in range(W):
    T_dic[tuple([T[i][j] for i in range(H)])] += 1

for k, v in S_dic.items():
    if T_dic[k] != v:
        print("No")
        exit()
print("Yes")