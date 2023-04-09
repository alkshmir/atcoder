

A, B = [int(s) for s in input().split()]
cnt = 0
while (A != B):
    #print(A, B, cnt)
    if A > B:
        if A % B == 0:
            cnt += A//B - 1
            A = B
        else:
            cnt += A//B
            A = A%B
    elif A < B:
        if B % A == 0:
            cnt += B//A - 1
            B = A
        else:
            cnt += B//A
            B = B%A
print(cnt)