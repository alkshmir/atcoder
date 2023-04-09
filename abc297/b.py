S = input()

b_pos = []
r_pos = []

for i, s in enumerate(S):
    if s == "B":
        b_pos.append(i+1)
    if s == "R":
        r_pos.append(i+1)
    if s == "K":
        k_pos = i+1

if b_pos[0] %2 == b_pos[1] %2:
    print("No")
    exit()

if r_pos[0] < k_pos < r_pos[1]:
    print("Yes")
else:
    print("No")
