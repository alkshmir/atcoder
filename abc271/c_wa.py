from collections import deque

N = int(input())
a = [int(s) for s in input().split()]

a = sorted(a)
q = deque()
for s in a:
    q.append(s)

cnt = 0
while(True):
    #print(i, cnt, a)

    if len(q)>0 and q[0] == cnt+1:
        cnt += 1
        q.popleft()
    else:
        if len(q) >= 2:
            # うしろ２つ売る
            #print(a.pop(), "を売った")
            #print(a.pop(), "を売った")
            q.pop()
            q.pop()
            cnt += 1
        else:
            break

print(cnt)