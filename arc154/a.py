# マジで解説読んでも意味がわからないけど小さい数字を片方に寄せればいいらしい

N = int(input())
A = [s for s in input()]
B = [s for s in input()]

for i in range(N):
    if int(A[i]) < int(B[i]):
        A[i], B[i] = B[i], A[i]

print(int(''.join(A))*int(''.join(B)) % 998244353)

