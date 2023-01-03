# 1つめの操作で塗るマスはy-x=B-Aを満たす
# 2つ目の操作で塗るマスは、y+x=A+Bを満たす
# P<=i<=Q, R<=j<=Sなる(i,j)で上のいずれかの式が満たされるなら黒、そうでなければ白
# 計算量はO((Q-P)*(S-R))
N, A, B = [int(s) for s in input().split()]
P, Q, R, S = [int(s) for s in input().split()]

for i in range(P, Q+1):
    for j in range(R, S+1):
        if j-i == B - A or j+i == A+B:
            print("#", end='')
        else:
            print('.', end='')
    print()
