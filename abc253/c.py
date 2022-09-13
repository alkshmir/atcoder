from collections import defaultdict
import bisect
Q = int(input())

S = defaultdict(int)
S_list = []
for _ in range(Q):
    q = [s for s in input().split()]
    command = q[0]
    if command == '1':
        x = int(q[1])
        if x not in S:
            #pos = bisect.bisect(S_list, q[1])
            bisect.insort(S_list, x)
        S[x] += 1
    elif command == '2':
        x = int(q[1])
        S[x] -= min(int(q[2]), S[x])
        if S[x] == 0:
            del S[x]
            i = bisect.bisect_left(S_list, x)
            if i != len(S_list) and S_list[i] == x:
                del S_list[i]
        
    elif command == '3':
        print(S_list[-1] - S_list[0])