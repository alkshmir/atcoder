# i=0からi=Nまで順にためせばよくね？
# と思ったがそうするとO(N^2)なので間に合わない

N = int(input())
T = input()
S = [None for _ in range(N)]
for i in range(N+1):
    invalid = False
    for j in range(i):
        S[j] = T[j]
    cnt = i
    for j in range(N):
        if S[-1-j] is None:
            S[-1-j] = T[cnt+j]
        elif S[-1-j] != T[cnt+j]:
            invalid = True
            break
    cnt += N
    if invalid:
        continue
    for j in range(N-i):
        if S[-(N-i)+j] is None:
            S[-(N-i)+j] = T[cnt+j]
        elif S[-(N-i)+j] != T[cnt+j]:
            invalid = True
            break
    if not invalid:
        print(S, i)
        exit()
    print(S)
print(-1)
