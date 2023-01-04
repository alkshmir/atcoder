# SとTが同じ数字の桁のところはUを0にしても1にしてもUとS,Tの距離の差は変わらない
# 従ってSとTが異なる数字の場所のみがハミング距離の増減に関わる。
# SとUのハミング距離が1増え、UとTのハミング距離が1減るか、その逆しか起こらない
# （つまり差は2ずつしか増減しない）ので、
# Sと0, Tと0のハミング距離の和が偶数でないとUは存在しない
# この時、SとTの数字が異なる小さい桁から1を立てていけば良い

N = int(input())
S = input()
T = input()
# S, Uのハミング距離
S_U = 0
T_U = 0
for i in range(N):
    if S[i] == '1':
        S_U += 1
    if T[i] == '1':
        T_U += 1
if (S_U + T_U) % 2:
    print(-1)
    exit()
U = ["0" for _ in range(N)]
cnt = 0
for i in range(N-1, -1, -1):
    if cnt == abs(S_U-T_U)//2:
        break
    if S_U > T_U:
        # Tが0でSが1のところを小さい桁から立てる
        if T[i] == '0' and S[i] == '1':
            U[i] = '1'
            cnt += 1
    else:
        if S[i] == '0' and T[i] == '1':
            U[i] = '1'
            cnt += 1
print("".join(U))