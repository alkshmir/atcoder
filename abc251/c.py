import numpy as np

N = int(input())

S = []
T = []
originals = set()
filtered_idx = []

for i in range(N):
    tmp = input().split()
    S.append(tmp[0])

    if tmp[0] not in originals:
        originals.add(tmp[0])
        T.append(int(tmp[1]))
    else:
        T.append(0)


print(np.argmax(T)+1)