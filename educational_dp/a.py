from cmath import inf


N = int(input())
h = [0] + [int(s) for s in input().split()]

c = [inf for _ in range(N+1)]
c[0] = 0
c[1] = 0
c[2] = abs(h[2] - h[1])
for i in range(2, N):
    #print("i: ", i)
    c[i+1] = min(c[i] + abs(h[i+1]-h[i]), c[i-1] + abs(h[i+1]-h[i-1]))
    #print("c: ", c)

print(c[-1])
