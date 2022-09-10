import itertools
N, M = [int(s) for s in input().split()]
S = []
for _ in range(N):
    S.append(input())
T = []
for _ in range(M):
    T.append(input())
T = set(T)
found = False

for s in itertools.permutations(S):
    username = '_'.join(s)
    if 3<=len(username)<=16  and username not in T:
        found = True
        break
    nokori = 16 - len(username)
    for j in range(nokori+1):
        for basho in itertools.combinations_with_replacement(range(N-1), j):
            # _ を増やす
            tmp_s = list(s)
            for n in basho:
                tmp_s[n] += '_'
            
            username = '_'.join(tmp_s)
           
            if 3<=len(username)<=16 and username not in T:
                found = True
                break
        if found:
            break

    if found:
        break

        
if found:
    print(username)
else:
    print(-1)