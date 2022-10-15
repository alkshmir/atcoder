from decimal import Decimal, ROUND_HALF_UP

X, K = [int(s) for s in input().split()]

for i in range(K):
    #X = int(round(X, -i))
    X = int(Decimal(X).quantize(Decimal('1e{}'.format(i+1)), rounding=ROUND_HALF_UP))
    #print(X)

print(X)