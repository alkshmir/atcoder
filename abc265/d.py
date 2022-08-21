N, P, Q, R = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

#S = [] # 累積和
S = set()

s = 0
S.add(s)
for i in range(N):
    s += A[i]
    S.add(s)

#print(list(S)[0])

list_S = list(S)
for x in range(N):
    if list_S[x] + P in S:
        Sy = list_S[x] + P
        if Sy + Q in S:
            Sz = Sy + Q
            if Sz + R in S:
                print("Yes")
                exit()
print("No")
