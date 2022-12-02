N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
B = [int(s) for s in input().split()]

candidates = [set() for _ in range(N)]
candidates[0].add('a')
candidates[0].add('b')
for i in range(N-2):
    # iばんめにaを選ぶ
    if 'a' in candidates[i]:
        if abs(A[i+1] - A[i]) <= K:
            if abs(A[i+2]- A[i+1]) <= K or abs(B[i+2] - A[i+1]) <= K:
                candidates[i+1].add('a')
        if abs(B[i+1] - A[i]) <= K:
            if abs(B[i+2] - B[i+1]) <= K or abs(A[i+2] - B[i+1]) <= K:
                candidates[i+1].add('b')
    
    if 'b' in candidates[i]:
        if abs(B[i+1] - B[i]) <= K:
            if abs(B[i+2] - B[i+1]) <= K or abs(A[i+2] - B[i+1]) <= K:
                candidates[i+1].add('b')
        if abs(A[i+1] - B[i]) <= K:
            if abs(A[i+2]- A[i+1]) <= K or abs(B[i+2] - A[i+1]) <= K:
                candidates[i+1].add('a')
    #print(candidates)
    if len(candidates[i+1]):
        continue
    #print(i, abs(A[i+1] - A[i]), abs(B[i+1] - A[i]), abs(B[i+1] - B[i]), abs(A[i+1] - B[i]))
    #print(i, candidates[i], candidates[i+1])
    print("No")
    exit()
    
print("Yes")