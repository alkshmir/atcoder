# 回転は4回まで
# 一回あたり10^4回なので全探索で十分間に合う
N = int(input())
A = []
for _ in range(N):
    A.append([int(s) for s in input().split()])

B = []
for _ in range(N):
    B.append([int(s) for s in input().split()])


for _ in range(4):
    A_new = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            A_new[i][j] = A[N-1-j][i]
    #print(A_new)
    # match
    flag = True
    for i in range(N):
        for j in range(N):
            if A_new[i][j] == 1 and B[i][j] != 1:
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Yes")
        exit()
    A = A_new
print("No")