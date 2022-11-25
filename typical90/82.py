L, R = [int(s) for s in input().split()]
def f(n):
    return n*(n+1)//2
cnt = 0
for i in range(1, 20):
    if not (R < 10**(i-1) or L >= 10**(i)):
        cnt += i*(f(min(10**(i)-1, R))-f(max(10**(i-1), L)-1))
    #print(i, cnt)
print(cnt % (10**9+7))