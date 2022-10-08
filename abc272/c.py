N = int(input())
A = [int(s) for s in input().split()]
 
gu = []
ki = []
for a in sorted(A, reverse=True):
    if a % 2:
        ki.append(a)
    else:
        gu.append(a)
 
#print(gu)
#print(ki)
gu = sorted(gu, reverse=True)
ki = sorted(ki, reverse=True)
 
 
m = -1
if len(gu) >= 2:
    m = max(m, gu[0] + gu[1])
 
if len(ki) >= 2:
    m = max(m, ki[0] + ki[1])
 
print(m)