# 左端から書き換えていけば良い(左端と右端は１回しか書き換えられないが、そのほかは２回書き換えられる)
import math
N = int(input())
S = [s for s in input()]

for i in range(math.ceil(N/2)-1):
    s = S[i]
    t = S[-i-1]
    if s == 'B' and t == 'A':
        S[i] = 'A'
        S[i+1] = 'B'
    elif s == 'A' and t == 'B':
        #print("No")
        #exit()
        pass
    elif s == 'A' and t == 'A':
        if S[i+1] == 'A' and S[-i-2] == 'B':
            S[i+1] = 'B'
#print(S)
for i in range(math.ceil(N/2)-1):
    s = S[-i-1]
    t = S[i]
    if s == 'A' and t == 'B':
        S[-i-1] = 'B'
        S[-i-2] = 'A'
    elif s == 'B' and t == 'A':
        pass
    elif s == 'B' and t == 'B':
        if S[-i-2] == 'B' and S[i+1] == 'A':
            S[-i-2] = 'A'
#print(S)

for i in range(N//2):
    if S[i] != S[-i-1]:
        print("No")
        exit()
print("Yes")