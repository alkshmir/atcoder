S = input()
T = input()

pre = [False for _ in range(len(T)+1)]
suf = [False for _ in range(len(T)+1)]

pre[0] = True
suf[0] = True
for i in range(len(T)):
    if S[i] == T[i] or S[i] == '?' or T[i] == '?':
        pre[i+1] = True
    else:
        break

for i in range(len(T)):
    if S[-i-1] == T[-i-1] or S[-i-1] == '?' or T[-i-1] == '?':
        suf[i+1] = True
    else:
        break

#print(pre)
#print(suf)
for i in range(len(T)+1):
    if pre[i] and suf[len(T)-i]:
        print("Yes")
    else:
        print("No")

