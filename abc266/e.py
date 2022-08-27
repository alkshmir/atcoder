N = int(input())

f = [0, 3.5]
for n in range(2, N+1):
    f.append(
        1/6 * max(1, f[n-1]) + 1/6 * max(2, f[n-1]) + 1/6 * max(3, f[n-1]) + 1/6 * max(4, f[n-1]) + 1/6 * max(5, f[n-1]) + 1/6 * max(6, f[n-1]) 
    )
print(f[-1])