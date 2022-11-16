N, L = [int(s) for s in input().split()]

cnt = [None for _ in range(N+1)]
cnt[0] = 1
for i in range(1, N+1):
    cnt[i] = cnt[i-1] 
    if i - L >= 0:
        cnt[i] += cnt[i-L]

print(cnt[-1]%(10**9+7))