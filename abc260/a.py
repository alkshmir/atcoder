S = input()
chars = set(S)

cnt = [0 for _ in range(len(chars))]

for i, c in enumerate(chars):
    for s in S:
        if s == c:
            cnt[i] += 1

#print(cnt)
flag = False
for i, c in enumerate(cnt):
    if c == 1:
        print(list(chars)[i])
        flag =True
        break

if not flag:
    print(-1)