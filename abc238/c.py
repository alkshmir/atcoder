#f(1) = 1, f(2) = 2
# f(10) = 1, f(11) = 2
# f(20) = 11
# n が i けたのとき、f(n) = n - 10^(i-1) + 1

N = int(input())
r = len(str(N))
ans = 0
for i in range(1, r+1):
    if i == r:
        n = N
    else:
        n = 10**(i)-1
    ans += n*(n+1)//2 - (10**(i-1)-1)*10**(i-1)//2 + (n-10**(i-1)+1)*(-10**(i-1)+1)
    ans %= 998244353
    #print(ans)
print(ans)