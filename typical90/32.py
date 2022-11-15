import math
import itertools
N = int(input())
A = []
for _ in range(N):
    A.append([int(s) for s in input().split()])

M = int(input())
blacklist = set()
for _ in range(M):
    x, y = [int(s) for s in input().split()]
    blacklist.add((x-1, y-1))

def isInBlacklist(runners):
    for i in range(N-1):
        if tuple(sorted([runners[i], runners[i+1]])) in blacklist:
            return True
    return False
score = math.inf
for runner in itertools.permutations(range(N)):
    if isInBlacklist(runner):
        continue
    
    score = min(sum([A[n][i] for i, n in enumerate(runner)]), score)
    #print(runner, score)
if score != math.inf:
    print(score)
else:
    print(-1)
    