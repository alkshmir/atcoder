H, W = [int(s) for s in input().split()]
A = []
for _ in range(H):
    A.append([int(s) for s in input().split()])

row = [] # i行目の合計
col = [] # j列目の合計
for i in range(H):
    row.append(sum(A[i]))
for j in range(W):
    col.append(sum([A[i][j] for i in range(H)]))

#ans = []
for i in range(H):
    #ans.append([row[i] + col[j] for j in range(W)])
    print(" ".join([str(row[i] + col[j]-A[i][j]) for j in range(W)]))

