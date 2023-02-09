# ジグザグに進めばいいので、高々3手で終わりそう
# 1手で行けるかどうかは自明である
# 2手以内で行ける領域は、次の領域の和集合である
#  a+bの偶奇が一致する領域
#  |a+b - (c+d)| <=3
#  |(a-b) - (c-d)| <=3
#  |a-c| + |b-d| <= 6
# それ以外は3手

a, b = [int(s) for s in input().split()]
c, d = [int(s) for s in input().split()]

if a == c and b == d:
    print(0)
elif a+b == c+d or a-b == c-d or abs(a-c) + abs(b-d) <= 3:
    print(1)
elif (a+b)%2 == (c+d)%2 or abs(a+b - (c+d)) <= 3 or abs((a-b) - (c-d)) <= 3 or abs(a-c)+abs(b-d) <= 6:
    print(2)
else:
    print(3)