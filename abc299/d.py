# S_1 = 0, S_N = 1なのでi=2からi=N-1のどこかで0と1がきりかわるのが絶対に1回以上ある。
# 真ん中が0のとき、左側に切り替わりポイントがない可能性がある、右側には必ずある。
# 真ん中が1のときは、逆に次に左側を調べていく
# こんな感じで2分探索すると、見つかりそう

N = int(input())
left = 0
right = N - 1

for _ in range(20):
    if left == right - 1:
        print('!', left + 1)
        break
    middle = (left + right) // 2
    print('?', middle+1)
    v = int(input())
    

    if v == 0:
        left = middle
    else:
        right = middle