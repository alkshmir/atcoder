# 山札から2つの#に入る数字の組み合わせを選ぶやり方ではO(N^2)になって間に合わない
# 同じ種類の数字が複数枚(K枚)あるので、上の組み合わせの中には
# 同じ数字のペアがたくさんある。このペアに対する高橋君、青木君のスコアは同じであり、
# したがって勝敗も同じである。
# 数字のペアは9*9通りしかなく、それぞれのペアに対し勝敗はO(max(len(S), D))の計算で決めることができるので、
# ある数字のペアとなる場合は何通りあるか？を調べればよい(Dは登場する数字の種類で今回はD=9)
# これは、まだ場に出ていない数字の個数を数えておくことによって実現可能である

K = int(input())
S = input()[:-1]
T = input()[:-1]

def score(S: str) -> int:
    cnt = [0 for _ in range(10)]
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10**cnt[i]
    return ans

cnt = [K for _ in range(10)]
for c in S:
    cnt[int(c)] -= 1
for c in T:
    cnt[int(c)] -= 1


ans = 0
for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(S + str(i)) > score(T + str(j)):
            ans += cnt[i] * cnt[j]

for i in range(1, 10):
    if cnt[i] < 2:
        continue
    if score(S + str(i)) > score(T + str(i)):
        ans += cnt[i] * (cnt[i]-1)

print(ans/((9*K - 8)*(9*K - 9)))