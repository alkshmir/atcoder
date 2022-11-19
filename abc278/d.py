N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())
query = []
for _ in range(Q):
    query.append([int(s) for s in input().split()])

start = None
offset = [0 for _ in range(N)]
for q in query:
    if q[0] == 1:
        start = q[1]
    elif q[0] == 2:
        if start is not None:
            A[q[1]] = start + q[2]
            
        else:
            A[q[1]] += q[2]
    elif q[0] == 3:
        if dirty[q[1]]:
            print(A[q[1]])
        else:
            print(A[q[1]] + start)