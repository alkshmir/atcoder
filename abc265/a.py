x, y, n = [int(s) for s in input().split()]

ans = 0

if x >= y/3:
    ans += int(n / 3) * y
    ans += (n % 3) * x 
else:
    ans += x * n

print(ans)