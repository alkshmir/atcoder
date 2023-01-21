N, P, Q, R, S = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]
ans = A[:P-1] + A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:]
print(" ".join([str(i) for i in ans]))