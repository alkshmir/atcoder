N = int(input())

if N % 2 != 0:
    exit()

for i in range(2**N):
    # 0と1の数が等しい
    cnt = 0
    for j in range(N):
        if (i >> j) & 1:
            cnt += 1
    if cnt * 2 != N:
        continue

    # 0の出てきた数-1の出てきた数 > 0
    s = 0
    valid = True
    for j in range(N-1, -1, -1):
        if (i >> j) & 1:
            s -= 1
        else:
            s += 1
        if s < 0:
            valid = False
            break
    if not valid:
        continue
    
    brackets = []
    for j in range(N-1, -1, -1):
        if (i >> j) & 1:
            brackets.append(')')
        else:
            brackets.append('(')

    print(''.join(brackets))