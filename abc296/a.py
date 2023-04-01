N = int(input())
S = input()

c = S[0]
for s in S[1:]:
    if s == c:
        print("No")
        exit()
    c = s
print("Yes")