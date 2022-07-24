N = int(input())
A = [0]
B = [0]
C = [0]
for _ in range(N):
    a,b,c = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)
    C.append(c)

h = [{'a':0, 'b':0, 'c':0} for _ in range(N+1)]
h[1] = {'a':A[1], 'b':B[1], 'c':C[1]}
for i in range(1,N):
    h[i+1]= {
        'a': A[i+1] + max(h[i]['b'], h[i]['c']),
        'b': B[i+1] + max(h[i]['a'], h[i]['c']),
        'c': C[i+1] + max(h[i]['a'], h[i]['b'])
    }

print(max(h[-1].values()))
