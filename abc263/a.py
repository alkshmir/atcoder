a, b, c, d, e = [int(s) for s in input().split()]

s = set([a, b, c, d, e])

if len(s) == 2:
    cnt = 0
    for t in [a, b, c, d, e]:
        if t == list(s)[0]:
            cnt += 1
    if cnt in [2, 3]:
        print("Yes")
    else:
        print("No")
else:
    print("No")