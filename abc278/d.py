N = int(input())
A = [int(s) for s in input().split()]
Q = int(input())
query = []
for _ in range(Q):
    query.append([int(s) for s in input().split()])

offset = None
drift = [0 for _ in range(N)]
dirty = []
for q in query:
    if q[0] == 1:
        offset = q[1]
        for d in dirty:
            drift[d] = 0
        dirty = []
    elif q[0] == 2:
        drift[q[1]-1] += q[2]
        dirty.append(q[1]-1)
    elif q[0] == 3:
        # A[q[1]]の値が正しいとき
        if offset is not None:
            print(drift[q[1]-1] + offset)
        else:
            print(A[q[1]-1] + drift[q[1]-1])