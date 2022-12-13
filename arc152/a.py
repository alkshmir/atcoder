N, L = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
edge = 0
isu = [False for _ in range(L+1)]
for a in A:
    edge += 1
    #print(edge)
    if a == 2 and edge >= L:
        print("No")
        exit()
    # edgeに座る
    for _ in range(a):
        if edge <= L:
            isu[edge] = True
        edge += 1
    #print(isu)

print("Yes")