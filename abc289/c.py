# 選んだ集合の和集合に、1~N全て含まれる
# これは10回計算すればいい
# 全体で(2^M -1 )* 10 買いぐらいで10^5回ぐらいで間に合う

N, M = [int(s) for s in input().split()]
S = []

for i in range(M):
    _ = input()
    S.append(set([int(s) for s in input().split()]))

all = set(range(1, N+1))
cnt = 0
for i in range(2**M):
    wa = set()
    for j in range(M):
        if (i >> j) & 1:
            wa |= S[j]
    if wa == all:
        cnt += 1
print(cnt)