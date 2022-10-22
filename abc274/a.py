from decimal import Decimal, ROUND_HALF_UP

A, B = [int(s) for s in input().split()]
S = B/A

s = Decimal(S).quantize(Decimal('1e{}'.format(-3)), rounding=ROUND_HALF_UP)
print(s)