# 解説読んだらgcdを使って傾きが同じかどうかを判別していたけど、普通に割り算するだけでACしてしまった。
from itertools import combinations
from collections import defaultdict

def lineparams(x1, y1, x2, y2):
    if x1 != x2:
        a = (y2 - y1) / (x2 - x1)
        #b = y1 - x1 * a
    else:
        a = None
        #b = x1
    #return (a, b)
    return a
N = int(input())
coods = []
for _ in range(N):
    coods.append([int(s) for s in input().split()])

lines = defaultdict(int)
for i, j in combinations(range(N), 2):
    x1, y1 = coods[i]
    x2, y2 = coods[j]
    #print(lineparams(x1, y1, x2, y2))
    lines[lineparams(x1, y1, x2, y2)] += 1
print(len(lines)*2)