from collections import defaultdict
N = int(input())
S = input()

d = defaultdict(list)
for i, c in enumerate(S):
    d[c].append(i)
#d_diff = defaultdict(set)
for k, v in d.items():
    d[k] = []
    for i in range(len(v)-1):
        d[k].append(v[i+1]-v[i])

#for i in range(1, N):
#    for k, v in d.items():
for i in range(1, N):
    ans = N
    for value in d.values():
        l = 0
        for v in value:
            if v != i:
                l += 1
        ans = min(ans, l)
    print(ans)