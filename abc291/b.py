N = int(input())
X = [int(s) for s in input().split()]
X.sort()

print(sum(X[N:-N])/(3*N))