N = int(input())
A = []
for i in range(N):
    A.append([int(_) for _ in list(input())])

#print(A)
# initial point
init = [(i,j) for i in range(N) for j in range(N)]

up = []
down =[]
right = []
left = []
ur =[]
ul = []
dr = []
dl = []
for start in init:
    # ue
    tmp = ''
    for i in range(N):
        tmp += str(A[start[0]][(start[1]-i)%N])
    up.append(int(tmp))

    # down
    tmp = ''
    for i in range(N):
        tmp += str(A[start[0]][(start[1]+i)%N])
    down.append(int(tmp))

    # right
    tmp = ''
    for i in range(N):
        tmp += str(A[(start[0] +i)%N][start[1]])
    right.append(int(tmp))

    # left
    tmp = ''
    for i in range(N):
        tmp += str(A[(start[0] -i)%N][start[1]])
    left.append(int(tmp))

    # ur
    tmp = ''
    for i in range(N):
        tmp += str(A[(start[0] +i)%N][(start[1] +i)%N])
    ur.append(int(tmp))

    # dr
    tmp = ''
    for i in range(N):
        tmp += str(A[(start[0] +i)%N][(start[1] -i)%N])
    dr.append(int(tmp))

    # ul
    tmp = ''
    for i in range(N):
        tmp += str(A[(start[0] -i)%N][(start[1] +i)%N])
    ul.append(int(tmp))

    # dl
    tmp = ''
    for i in range(N):
        tmp += str(A[(start[0] -i)%N][(start[1] -i)%N])
    dl.append(int(tmp))

l = up + down + right + left + ur + ul + dr + dl
print(max(l))