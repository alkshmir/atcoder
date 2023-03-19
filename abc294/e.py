# v_{i,j}をソートしていもす法的なことをすればうまくいきそうな気がする
from operator import attrgetter
class run_length(object):
    def __init__(self, v, x, end, type):
        self.v = v
        self.start = x
        self.end = end
        self.type = type

L, N1, N2 = [int(s) for s in input().split()]
a = []
b = []
x = 0
for _ in range(N1):
    v, l = [int(s) for s in input().split()]
    
    a.append(run_length(v, x, x+l, 'a'))
    x += l
x = 0
for _ in range(N2):
    v, l = [int(s) for s in input().split()]
    b.append(run_length(v, x, x+l, 'b'))
    x += l

events = a+b
events.sort(key=attrgetter('start'))
last_a_event = events[0]
last_b_event = events[1]
cnt = 0
if last_a_event.v == last_b_event.v:
    cnt += min(last_a_event.end, last_b_event.end) - max(last_a_event.start, last_b_event.start)
#print(last_event.start, last_event.end, last_event.v, last_event.type)

for e in events[2:]:
    #print(e.start, e.end, e.v, e.type)
    if e.type == 'a':
        if e.v == last_b_event.v:
            # かぶっている部分を出す
            cnt += min(e.end, last_b_event.end) - max(e.start, last_b_event.start)
            #print(cnt)
        last_a_event = e
    elif e.type == 'b':
        if e.v == last_a_event.v:
            cnt += min(e.end, last_a_event.end) - max(e.start, last_a_event.start)
        last_b_event = e
print(cnt)