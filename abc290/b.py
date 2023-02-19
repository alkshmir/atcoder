N, K = [int(s) for s in input().split()]
S = input()

cnt = 0
for s in S:
    if s == 'o':
        cnt += 1
        if cnt > K:
            print('x', end='')
        else:
            print('o', end='')
    else:
        print('x', end='')
print()