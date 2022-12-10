S = input().split()
T = input().split()
c = 0
for s,t in zip(S,T):
    if s != t:
        c += 1
if c in [0, 3]:
    print("Yes")
else:
    print("No")