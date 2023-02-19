N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
A.sort()

mex = 0
if list(set(A))[:K] == list(range(K)):
    print(K)
    exit()
for a in list(set(A))[:K]:
    if mex == a:
        mex += 1
    else:
        print(mex)
        exit()
print(mex)