S = input()
n = len(S)
cnt = 0
tmp_S = S[::-1]
i = 0
while i < n:
    if tmp_S[i] == '0':
        if i != n-1 and tmp_S[i+1] == '0':
            i += 1
        cnt += 1
    else:
        cnt += 1
    i += 1
print(cnt)
