N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())
query = []
for _ in range(Q):
    query.append([int(s) for s in input().split()])

for q in query:
    if q[0] == 1:
        k = q[1]
        x = q[2]
        A[k-1] = x
    elif q[0] == 2:
        k = q[1]
        print(A[k-1])