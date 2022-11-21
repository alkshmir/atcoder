N, K = [int(s) for s in input().split()]

N_8 = 0
for i, s in enumerate(reversed(str(N))):
    N_8 += int(s)*8**i

#print(N_8)
for i in range(K):
    N_9 = 0
    for j in range(21,-1,-1):
        N_9 += (N_8 // (9**(j)))*10**j
        N_8 -= (N_8 // (9**(j)))*9**j

    #print(N_9)
    N_8 = 0
    for j, s in enumerate(reversed(str(N_9))):
        if s == '8':
            s = '5'
        N_8 += int(s)*8**j

N = 0
for i in range(21, -1, -1):
    N += (N_8 // (8**i))*10**i
    N_8 -= (N_8 // (8**i))*8**i
print(N)