N = int(input())
S = []
for _ in range(N):
    S.append(input())

for s in S:
    if s[0] not in ['H', 'D', 'C', 'S']:
        print("No")
        exit()

for s in S:
    if s[1] not in ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']:
        print("No")
        exit()

S_set = set(S)
if len(S) != len(S_set):
    print("No")
    exit()

print("Yes")
