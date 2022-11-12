N, X = [int(s) for s in input().split()]
P = [int(s) for s in input().split()]

for i in range(N):
    if P[i] == X:
        print(i+1)