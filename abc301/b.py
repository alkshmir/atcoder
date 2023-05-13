N = int(input())
A = [int(s) for s in input().split()]

A_ans = [a for a in A]
ins = []
for i in range(N-1):
    if abs(A[i] - A[i+1]) == 1:
        continue

    if A[i] < A[i+1]:
        ins.append((i, list(range(A[i]+1, A[i+1]))))
    elif A[i] > A[i+1]:
        ins.append((i, list(range(A[i]-1, A[i+1], -1))))

#print(ins)
offset = 0
for item in ins:
    idx = item[0] + offset
    lst = item[1]
    A_ans = A_ans[:idx+1] + lst + A_ans[idx+1:]
    #print(A_ans)
    offset += len(lst)
print(' '.join([str(i) for i in A_ans]))