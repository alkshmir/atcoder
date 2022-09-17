N = int(input())

n2 = str(bin(N))
n2 = n2[2:]
#print(n2)
i_list = []
for i, n in enumerate(n2[::-1]):
    if n == '1':
        i_list.append(i)

#print(i_list)
ans = []
for i in range(2 ** len(i_list)):
    acc = 0
    for j in range(len(i_list)):
        if ((i) >> j) & 1:
            acc += 2**(i_list[j-1])
    #print(bin(acc))
    ans.append(acc)

for a in sorted(ans):
    print(a)
