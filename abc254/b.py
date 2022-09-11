N = int(input())

a = [[None for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1):
        if j == 0 or j == i:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    #tmp = [str(k) for k in a[i]]
    for n, k in enumerate(a[i]):
        if k:
            if n != i:
                print(k, end=' ')
            else:
                print(k)
    #print(' '.join(tmp))
