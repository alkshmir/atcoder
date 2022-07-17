import numpy as np
N, X, Y, Z = [int(s) for s in input().split()]
A = np.array([int(s) for s in input().split()])
B = np.array([int(s) for s in input().split()])

passed = [False for _ in range(N)]

# suugaku goukaku
for i in np.argsort(-A, kind="stable")[:X]:
    passed[i] = True

cnt = 0
for i in np.argsort(-B, kind="stable"):
    if cnt == Y:
        break

    # not already passed
    if not passed[i]:
        passed[i] = True
        cnt += 1

cnt = 0
for i in np.argsort(-(A+B), kind="stable"):
    if cnt == Z:
        break
    if not passed[i]:
        passed[i] = True
        cnt += 1


#print(passed)
for i, p in enumerate(passed):
    if p:
        print(i+1)