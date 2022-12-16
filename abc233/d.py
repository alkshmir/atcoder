N, K = [int(s) for s in input().split()]
A = [int(s) for s in input().split()]

def count_subsequences(A, N, K):
    counter = 0
    sum = 0
    sum_count = {0: 1}  # store the number of times each sum appears

    for i in range(N):
        sum += A[i]
        if sum - K in sum_count:  # check if there is a sum that equals K
            counter += sum_count[sum - K]
        if sum in sum_count:
            sum_count[sum] += 1
        else:
            sum_count[sum] = 1

    return counter
print(count_subsequences(A, N, K))