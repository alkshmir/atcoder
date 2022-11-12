N = int(input())
S = []
for _ in range(N):
    S.append(input())

users = set()
for i in range(N):
    if S[i] in users:
        continue
    users.add(S[i])
    print(i+1)
