from itertools import combinations
N, K, D = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

su = [sum(nums) for nums in combinations(A, K)]
bai = []
for s in su:
    if s % D == 0:
        bai.append(s)
if len(bai) == 0:
    print(-1)
    exit()
print(max(bai))