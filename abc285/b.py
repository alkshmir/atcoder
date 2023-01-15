
N = int(input())
S = input()

for i in range(1, N):
    
    for k in range(1, N-i+1):
        if S[k-1] != S[k+i-1]:
            pass
        else:
            k -= 1
            break
        #l += 1
    #if invalid:
    #    break
    #l += 1
    
    print(k)