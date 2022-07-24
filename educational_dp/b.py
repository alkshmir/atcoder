from cmath import inf


N, K = [int(s) for s in input().split()]
h = [0] + [int(s) for s in input().split()]

c = [inf for _ in range(N+1)]
c[0] = 0
c[1] = 0
c[2] = abs(h[2] - h[1])
for i in range(2, N):
    #print("i: ", i)
    #print(list(range(max(i-K+1, 1), i+1)))
    options = [c[j] + abs(h[i+1]-h[j]) for j in range(max(i-K+1, 1), i+1)]
    c[i+1] = min(options)
    #print("c: ", c)

print(c[-1])
