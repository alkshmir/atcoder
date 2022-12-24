# 2000C4個数えてたら到底間に合わない。2000C3でも間に合わない。
# 2000^2ぐらいにしないといけない。
# xもyも異なる2点(x1, y1), (x2, y2)を選んで、(x1, y2)と(x2, y1)が存在するかを調べれば良い
# 存在するかどうかはHash mapなどを使えばO(1)で調べられる。
# よってO(N^2)で調べられた。
import itertools
N = int(input())
cood = set()
for _ in range(N):
    x, y = [int(s) for s in input().split()]
    cood.add((x, y))

cnt = 0
for p1, p2 in itertools.combinations(cood, 2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 or y1 == y2:
        continue
    if (x1, y2) in cood and (x2, y1) in cood:
        cnt += 1

print(cnt//2)