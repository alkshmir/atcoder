from collections import defaultdict
N, M = [int(s) for s in input().split()]
next_hop_larger = defaultdict(list)
next_hop_smaller = defaultdict(list)
for _ in range(M):
    a, b = [int(s) for s in input().split()]
    if a > b:
        next_hop_smaller[a].append(b)
    else:
        next_hop_larger[a].append(b)
    if b > a:
        next_hop_smaller[b].append(a)
    else:
        next_hop_larger[b].append(a)

cnt = 0
for i in range(1, N+1):
    if len(next_hop_smaller[i]) == 1:
        cnt += 1
print(cnt)