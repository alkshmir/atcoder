def swap(l: list, n:int, m:int):
    l[n], l[m] = l[m], l[n]
    return l

N = int(input())
P = [int(s) for s in input().split()]

for n in range(N-1, 0, -1):
    if P[n] < P[n-1]:
        break

#print('n=', n)
# ソート対象
sorted_p = P[n-1::]

tmp = sorted(sorted_p[1::], reverse=True)
for i, p in enumerate(tmp):
    if p < sorted_p[0]:
        #print(i)
        break
sorted_p = swap([sorted_p[0]] + tmp, 0, i+1)
#print(sorted_p)


ans = P[:n-1] + sorted_p
print(' '.join([str(n) for n in ans]))