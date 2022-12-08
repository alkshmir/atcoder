import copy
N = int(input())

paths = [1 for _ in range(9)]
for i in range(1, N):
    prev = copy.copy(paths)
    for j in range(9):
        if j == 0:
            paths[j] = (prev[j] + prev[j+1])%998244353
        elif j == 8:
            paths[j] = (prev[j-1] + prev[j])%998244353
        else:
            paths[j] = (prev[j-1] + prev[j] + prev[j+1])%998244353
print(sum(paths)%998244353)