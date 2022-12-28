T = int(input())

for _ in range(T):
    a, s = [int(s) for s in input().split()]
    if s-2*a < 0:
        print("No")
        continue
    #print(a & (s-2*a))
    if a & (s-2*a):
        print("No")
    else:
        print("Yes")