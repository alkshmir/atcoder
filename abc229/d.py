S = input()
K = int(input())
n = len(S)

cul_sum = [0]

for i in range(n):
    if S[i] == '.':
        d = 1
    else:
        d = 0
    cul_sum.append(cul_sum[-1] + d)
#print(cul_sum)

ans = 0
r = 0
for l in range(n):
    # S[l,r+1)をすべて 'X' に変えることが可能
    while(r<n and cul_sum[r+1] - cul_sum[l] <= K):
        r+=1
    #print(l, r, r-l)
    ans = max(ans, r-l)
print(ans)