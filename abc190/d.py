# 初項a, 公差1, 項数n, 末項l=a+n-1の等差数列の和は
# (a+l)*n/2 = (2*a+n-1)*n/2 = a*n + n*(n-1)/2 = N

# nについて解の公式を使ってとき、
# 平方根の中身が平方数となる条件を求めると
# -8N = (2a-1+m)(2a-1-m) mは整数
# と書けることが条件っぽい
# 8*Nの約数を求めて、そのペアの和(4a-2)を4で割ったあまりが
# 2であり、ペアの差(2m)が偶数であるようなペアの数の２倍が
# 答え
def find_factor(n: int):
    i = 1
    factors = set()
    while i * i <= n:
        if n % i == 0:
            factors.add((i, n//i))
        i += 1
    return factors
N = int(input())

factors = find_factor(N*8)
cnt = 0
for i, j in factors:
    if (j-i) % 2 == 0 and (i+j) % 4 == 2:
        cnt += 2
print(cnt)
