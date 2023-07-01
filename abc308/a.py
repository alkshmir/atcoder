S = [int(s) for s in input().split()]

for i in range(7):
    if not S[i] <= S[i+1]:
        print("No")
        exit()

for i in range(8):
    if not (100 <= S[i] <= 675):
        print("No")
        exit()
    if not (S[i] % 25 == 0):
        print("No")
        exit()

print("Yes")