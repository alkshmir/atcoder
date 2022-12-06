N = int(input())
S = [int(s) for s in input().split()]

A = []
cul = []
A.append(S[0])
cul.append(S[0])
for i in range(1, N):
    A.append(S[i] - S[i-1])
print(' '.join([str(a) for a in A]))