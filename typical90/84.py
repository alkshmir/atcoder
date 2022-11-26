N = int(input())
S = input()
all_cases = N * (N+1) // 2
llc = []
for i in range(N):
    if i == 0:
        llc.append([S[i], 1])
    else:
        if S[i] == llc[-1][0]:
            llc[-1][1] += 1
        else:
            llc.append([S[i],1])
#print(llc)
ans = all_cases
for c in llc:
    ans -= c[1] * (c[1]+1) // 2
print(ans)