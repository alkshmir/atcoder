# Aの中にiが出てくる回数をdup[i]とおく
# それぞれのAの要素を2数の積k*vに分解する(O(N*max(A)^1/2))
# 2 * dup[k] * dup[v]を加えていく
# よってO(N*max(A)^1/2)で計算できた。

from collections import defaultdict
N = int(input())
A = [int(s) for s in input().split()]
dup = defaultdict(int)
for a in A:
    dup[a] += 1
cnt = 0
done = defaultdict(bool)
for a in A:
    i = 1
    if done[a]:
        continue
    done[a] = True
    while i*i <= a:
        if a % i == 0:
            #d = defaultdict(int) # 使った回数
            #tmp = dup[i]
            #d[i] += 1
            #tmp *= max(0, dup[a//i])
            #d[a//i] += 1
            #tmp *= max(0, dup[a])
            #d[a] += 1
            tmp = dup[i] * dup[a//i] * dup[a]
            if i*i != a:
                tmp *= 2
            #print(a, i, a//i, tmp)
            cnt += tmp
        i+=1
print(cnt)

# 解けたけど、むずかった。最初i,j,kは被っちゃだめだと思って、何が間違っているのか分からなかった。
# 上の解法ではAを順番に舐めているけど、解説ではdupのkeyを順番に舐めていた。
# こうすることでdoneとかいう辞書も不要になるので、こちらの方がスマートっぽい。
# 最初に建てた方針は間違っていなかったものの、最初doneがなくて同じものを何回も数えてたので良くなかった。
# そこでi,j,kがかぶってるから答えよりも多い値が出てるんだと勘違いして、そこから時間がかかってしまった。
# 問題文をちゃんと読むのと、２つ以上変更点があるときに、テスト結果の変化が前の変更によるものなのか、今の変更によるものなのかを
# ちゃんと切り分ける。