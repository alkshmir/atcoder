l1, r1, l2, r2 = [int(s) for s in input().split()]

if r2 <= l1 or r1<= l2:
    print(0)
elif l1 <= l2 and r2 <= r1:
    print(r2-l2)
elif l2 <= l1 and l1 <= r2 and r2 <= r1:
    print(r2-l1)
elif l1 <= l2 and l2 <= r1 and r1 <= r2:
    print(r1-l2)
else:
    print(r1-l1)