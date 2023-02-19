# NとDが互いに素な場合は、D(K-1) mod Nが答え
# NとDが互いに素でなく、
# ii) D

import math
T = int(input())
for _ in range(T):
    N, D, K = [int(s) for s in input().split()]

    g = math.gcd(N, D)
    period = N // g
    offset = (K-1)//period
    print((D*(K-1))%N + (K-1)//period)
    '''
    if g == 1:
        print(D*(K-1) % N)
    
    else:
        if D >= N:
            print(K-1)
        else:
            period = N//D
            print((D*(K-1))%N + (K-1)//period)
    '''
'''
6 4 
0 1 2 3 4 5 
0   2   1 
'''