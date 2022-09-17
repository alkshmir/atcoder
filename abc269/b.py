S = []
for _ in range(10):
    S.append(input())

a = 10
b = 1
c= 10
d = 1
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            a = min(i+1, a)
            b = max(i+1, b)
            c = min(j+1, c)
            d = max(j+1, d)

print(a, b)
print(c, d)