import math
A, B = [int(s) for s in input().split()]
if A <= 2*B:
    print(A)
    exit()

t = math.pow( A/(2*B), 1/3 )
#print(round(t))
c = round(t**2 - 1)
if c != 0:
    print(min(A/math.sqrt(c+1) + c*B, A/math.sqrt(c)+ (c-1)*B, A/math.sqrt(c+2)+(c+1)*B))
else:
    print(min(A/math.sqrt(c+1) + c*B, A/math.sqrt(c+2)+(c+1)*B))