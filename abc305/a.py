N = int(input())

# pとp+5の間
p = (N//5) * 5
#print(p)
if abs(N-p) < abs(N-(p+5)):
    print(p)
else:
    print(p+5)