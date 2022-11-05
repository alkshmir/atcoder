from collections import defaultdict
N, M = [int(s) for s in input().split()]
A = []
B = []
cities = defaultdict(list)
for _ in range(M):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)
    cities[a].append(b)
    cities[b].append(a)

for i in range(1, N+1):
    print(len(cities[i]), end='')
    if len(cities[i]) > 0:
        print('', ' '.join([str(n) for n in sorted(cities[i])]))
    else:
        print()