import itertools
N, K = [int(s) for s in input().split()]
S = []
for _ in range(N):
    S.append(set(input()))

cnt_max = 0
for i in range(K,N+1):
    for s in itertools.combinations(S, i):
        union_set = s[0]
        for j in range(1,i):
            union_set = union_set | s[j]
        
        #print(s, union_set, len(s))

        ans = 0
        for c in union_set:
            cnt = 0
            for t in s:
                if c in t:
                    cnt += 1
            if cnt == K:
                ans += 1
        cnt_max = max(ans, cnt_max)

print(cnt_max)