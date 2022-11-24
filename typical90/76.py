import bisect
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

N = int(input())
A = [int(s) for s in input().split()]
A_sum = sum(A)
cumul = [A[0]]
for i in range(1, N):
    cumul.append(cumul[-1]+A[i])
for i in range(N):
    cumul.append(cumul[-1]+A[i])
cumul = [0] + cumul
#print(cumul)
if cumul[-1] % 20 != 0:
    print("No")
    exit()
for l in cumul[:-1]:
    r = index(cumul, cumul[-1]//20+l)
    if r is not None:
        print("Yes")
        exit()
print("No")