# imos法 いもす法かと思いきや、いもす法ではO(N+max(A))かかるので間に合わない
# いもす法では時系列でシミュレートをしているが、その代わりにログイン/ログアウトが起こる
# イベントの時刻をソートして、前のイベントが起きてから次のイベントが起こるまでの時間は
# ログイン人数が変わらないことを用いてログイン人数をカウントする。
# いもす法と同様に、ログイン・ログアウトした人物を区別しないのがややポイント。
# 計算量はO(NlogN)
from operator import attrgetter
class event():
    def __init__(self, time, type):
        self.time = time
        self.type = type

N = int(input())
events = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    events.append(event(a, 'login'))
    events.append(event(b+a, 'logout'))
    
events.sort(key=attrgetter('time'))
ans = [0 for _ in range(N+1)]
cnt = 1
last = events[0]
for e in events[1:]:
    #print(e.time, e.type)
    if e.type == 'login':
        ans[cnt] += e.time - last.time
        cnt += 1
    else:
        ans[cnt] += e.time - last.time
        cnt -= 1
    last = e
print(" ".join([str(n) for n in ans[1:]]))