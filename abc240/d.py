N = int(input())
A = [int(s) for s in input().split()]

values = []
dup = []
values.append(A[0])
dup.append(1)
cnt = 1
print(cnt)
for a in A[1:]:
    #values.append(a)
    if len(values) and a == values[-1]:
        dup[-1] += 1 
    else:
        values.append(a)
        dup.append(1)
    if len(values) and len(dup) and dup[-1] == values[-1]:
        d = dup[-1]
        #values = values[:-d]
        #dup = dup[:-d]
        values = values[:-1]
        dup = dup[:-1]
        cnt -= d
    cnt += 1
    print(cnt)
    #print(cnt, values, dup)
