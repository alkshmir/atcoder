N = int(input())
P = [0] + [0] + [int(s) for s in input().split()]

oya = P[-1]
gen = 1
while (oya != 1):
    #print(oya, gen)
    oya = P[oya]
    gen += 1
print(gen)