N, X = [int(s) for s in input().split()]
S = input()

node = X
move = []
for s in S:
    if s == 'U':
        if not move or move[-1] == 'U':
            move.append(s)
        else:
            move.pop()
    else:
        move.append(s)

for s in move:
    if s == 'U':
        node = node // 2
    elif s == 'L':
        node = node * 2
    elif s == 'R':
        node = node * 2 + 1
print(node)