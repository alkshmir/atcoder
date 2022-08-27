from random import randrange

N = 2 ** 10
sum = 0
for k in range(N):
    x = max(randrange(1, 7), randrange(1,7))
    sum += x

print(sum / N)
