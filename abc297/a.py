N, D = [int(s) for s in input().split()]
T = [int(s) for s in input().split()]

first = T[0]

for t in T[1:]:
    if t - first <= D:
        print(t)
        exit()
    first = t
print(-1)