import math
def solve(N):
    result = 0
    #for A in range(1, int(math.pow(N, 1/3))+1):
    A = 1
    while A*A*A <= N:
        #for B in range(A, int(math.pow(N/A, 1/2))+1):
        B = A
        while A*B*B <= N:
            C_max = int(math.floor(N / (A * B)))
            result += C_max - B + 1
            B += 1
        A += 1
    return result
N = int(input())
print(solve(N))