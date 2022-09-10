S = input()
T = input()

yes = True

if len(T) < len(S):
    print("No")
    exit()

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        yes = False
        break

if yes:
    print("Yes")
else:
    print("No")