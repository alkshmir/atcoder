N = int(input())
A = sorted([int(s) for s in input().split()])
B = sorted([int(s) for s in input().split()])

cost = 0
for a, b in zip(A, B):
    cost += abs(a-b)
print(cost)