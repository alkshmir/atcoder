A, B = [int(s) for s in input().split()]

n = 1
for i in range(40):
    if n >= B:
        print(i)
        break
    n += A-1
