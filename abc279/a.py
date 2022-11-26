S = input()

cnt = 0
for s in S:
    if s == 'v':
        cnt += 1
    elif s == 'w':
        cnt += 2
print(cnt)