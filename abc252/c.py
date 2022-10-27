N = int(input())
S = []
for _ in range(N):
    S.append([int(s) for s in list(input())])

time = []
for n in range(10):
    stopped = [False for _ in range(N)]
    for t in range(10*N+1):
        for i in range(N):
            if stopped[i]:
                continue
            if S[i][t % 10] == n:
                stopped[i] = True
                break
        if all(stopped):
            break
    time.append(t)

#print(time)
print(min(time))