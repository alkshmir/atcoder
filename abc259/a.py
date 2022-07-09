inp = [int(i) for i in input().split()]
N = inp[0]
M = inp[1]
X = inp[2]
T = inp[3]
D = inp[4]

#print(N, M, X, T, D)
if M >= X:
    print(T)
elif M < X:
    print(T- D*(X-M))
