S = input()
T = input()

t_idx = 0
for s in S:
    if s == T[t_idx]:
        t_idx += 1
    else:
        t_idx = 0
    if t_idx == len(T):
        print("Yes")
        exit()
print("No")