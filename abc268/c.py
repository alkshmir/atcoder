N = int(input())
p = [int(s) for s in input().split()]

c = [0 for _ in range(N)]
for idx_human in range(N):
    idx_food = p[idx_human]
    c[(idx_human-idx_food)%N] += 1
    c[(idx_human-idx_food-1)%N] += 1
    c[(idx_human-idx_food+1)%N] += 1

print(max(c))