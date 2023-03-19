def trans(i):
    if i == 0:
        return '.'
    else:
        return chr(64+i)

H, W = [int(s) for s in input().split()]
A = []
for _ in range(H):
    A.append([int(s) for s in input().split()])


for a in A:
    #ans.append([trans(i) for i in a])
    print(''.join([trans(i) for i in a]))
