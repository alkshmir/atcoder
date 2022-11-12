N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]

d = 0
for a, b in zip(A, B):
    d += abs(a-b)
if d <= K and (K-d)%2 == 0:
    print("Yes")
else:
    print("No")