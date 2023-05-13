import math
N = int(input())
S = input()

quarum = math.ceil(N / 2)
#print(quarum)
t = 0
a = 0
for s in S:
    if s == 'T':
        t += 1
    elif s == 'A':
        a += 1
    
    if t >= quarum:
        print("T")
        break
    if a >= quarum:
        print("A")
        break
