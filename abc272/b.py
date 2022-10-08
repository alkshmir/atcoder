from itertools import permutations


N, M = [int(s) for s in input().split()]

k = []
x = []
for _ in range(M):
    tmp = [int(s) for s in input().split()]
    k.append(tmp[0])
    x.append(tmp[1:])

friends = [[False for _ in range(N)] for _ in range(N)]

# 対角
for i in range(N):
    friends[i][i] = True
#print(friends)

for part in x:
    #print(list(permutations(part)))
    for i, j in permutations(part, 2):
        friends[i-1][j-1] = True

#print(friends)

ans = True
for f in friends:
    ans = all(f) and ans

if ans:
    print("Yes")
else:
    print("No")