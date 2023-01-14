H, W = [int(s) for s in input().split()]
A = []
for _ in range(H):
    A.append([s for s in input()])
Q = int(input())
aq = []
bq = []
for _ in range(Q):
    tmp = [int(s) for s in input().split()]
    aq.append(tmp[0])
    bq.append(tmp[1])

w12 = [0, 1]
for b in bq:
    for i in range(2):
        if w12[i] < b:
            w12[i] = b - w12[i]-1 #+ 1
        else:
            w12[i] = b + W - w12[i]-1 #+ 1
#print(w12)
h12 = [0, 1]
for a in aq:
    for i in range(2):
        if h12[i] < a:
            h12[i] = a - h12[i] -1#+ 1
        else:
            h12[i] = a + H - h12[i]-1 #+ 1
#print(h12)
map_h = [0] * H
for i in range(H):
    if Q%2:
        map_h[(h12[0] - i )%H] = i
    else:
        map_h[(h12[0] + i )%H] = i
map_w = [0] * W
for i in range(W):
    if Q%2:
        map_w[(w12[0] - i )%W] = i
    else:
        map_w[(w12[0] + i )%W] = i

for i in map_h:
    l = []
    for j in map_w:
        l.append(A[i][j])
    print("".join(l))