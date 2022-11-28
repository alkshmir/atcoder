from collections import deque
Q = int(input())
query = []
for _ in range(Q):
    query.append(input().split())

tutu = deque()
for q in query:
    if q[0] == '1':
        x = int(q[1])
        c = int(q[2])
        tutu.append([x, c])
    elif q[0] == '2':
        c = int(q[1])
        out = 0
        while(c > 0):
            if c <= tutu[0][1]:
                out += tutu[0][0] * c
                tutu[0][1] -= c
                c = 0
            else:
                out += tutu[0][0] * tutu[0][1]
                c -= tutu[0][1]
                tutu[0][1] = 0
            if tutu[0][1] == 0:
                tutu.popleft()
        print(out)
