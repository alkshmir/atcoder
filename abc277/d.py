from collections import defaultdict
N, M = [int(s) for s in input().split()]
A = sorted([int(s) for s in input().split()])

# 数字->group
group_mapping = dict()
groups = defaultdict(list)
# 重複度
#overlap = defaultdict(int)
group_sum = defaultdict(int)
for i in range(N):
    if i == 0:
        group_mapping[A[0]] = A[0]
        groups[A[0]].append(A[0])
    else:
        if A[i] - A[i-1] == 1 or A[i] == A[i-1]:
            #print(i, A[i], A[i-1])
            group_mapping[A[i]] = group_mapping[A[i-1]]
            groups[group_mapping[A[i]]].append(A[i])
        else:
            group_mapping[A[i]] = A[i]
            groups[A[i]].append(A[i])
    group_sum[group_mapping[A[i]]] += A[i]

# 0 とM-1をマージ
if 0 == A[0] and M-1 == A[-1]:
    for n in groups[group_mapping[M-1]]:
        groups[0].append(n)
    group_sum[0] += group_sum[group_mapping[M-1]]
    groups.pop(group_mapping[M-1])
    group_sum.pop(group_mapping[M-1])
#print(groups)
#print(group_mapping)


max_sum = 0
for k, v in group_sum.items():
    if v >= max_sum:
        max_sum = max(max_sum, v)
        max_sum_key = k
ans = 0
for k, v in group_sum.items():
    if k == max_sum_key:
        continue
    ans += v

print(ans)