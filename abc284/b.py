T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(s) for s in input().split()]
    cnt = 0
    for a in A:
        if a % 2 == 1:
            cnt += 1
    print(cnt)