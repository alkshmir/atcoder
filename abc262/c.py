N = int(input())
a = [0] + [int(s) for s in input().split()]

cnt = 0
# aとindexが同じものを数える
same = 0
for i in range(1, N+1):
    if a[i] == i:
        same += 1

cnt += int(same * (same-1) / 2)

# a[a[i]]の値がiであるものを数える
swap = 0
for i in range(1, N+1):
    #print("i: ",i)
    if a[i] != i and a[a[i]] == i:
        swap += 1
cnt += int(swap/2)
print(cnt)