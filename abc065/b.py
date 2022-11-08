N = int(input())

next_hop = {}

for i in range(1, N+1):
    next_hop[i] = int(input())

visited = set()

cnt = 0
now = 1
while True:
    if now in visited:
        print(-1)
        exit()
    if now == 2:
        break
    visited.add(now)
    now = next_hop[now]
    cnt += 1
print(cnt)