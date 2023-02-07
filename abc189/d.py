# 小さい桁からy_iが1になる場合の数を数えていく
# これをone[i]とおく
# 0になる場合の数は2^{i+1} - one[i]として求めればよい
# one[0] = 1
# one[i]が決まっているとき、one[i+1]を決めたい
# S_{i+1}がANDなら、y_{i+1}が1になるのはx_{i+1}が1かつy_iが1の時に限るので
# one[i+1]=one[i]

# S_{i+1}がORなら、y_{i+1}が1になるのはx_{i+1}が1またはy_iが1の場合なので
# (x_{i+1}, y_i) = (1, 1), (1,0), (0,1)の時をそれぞれ足して
# one[i+1] = one[i] + 1*(2^(i+1)-one[i]) + one[i] = one[i] + 2^(i+1)
# まとめると
# one[i+1] = S_{i+1}*one[i] + !S_{i+1}*(one[i] + 2^(i+1))
#          = one[i] + !S_{i+1}*2^(i+1)
# よって、ORの時は2^(i+1)を加えていけばいい

N = int(input())
S = []
for _ in range(N):
    s = input()
    if s == "OR":
        S.append(False)
    else:
        S.append(True)

cnt = 1
for i in range(N):
    if S[i] == False:
        cnt += 2**(i+1)
print(cnt)


