N = int(input())
A, B, C = [int(s) for s in input().split()]

min_coins = 10000
for i in range(10000):
    for j in range(10000-i):
        if (N - A*i - B*j) < 0 or (N - A*i - B*j) % C != 0:
            continue
        k = (N - A*i - B*j) // C
        min_coins = min(min_coins, i+j+k)
print(min_coins)