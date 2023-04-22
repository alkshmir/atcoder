# -がないときは-1を出力し、以降-が1個以上あるときを考える
# 連続するoが一番多いところを探す、
# その端はかならず-なので、連続するoの数を出力すればいい。
N = int(input())
S = input()

if '-' not in S:
    print(-1)
    exit()
if 'o' not in S:
    print(-1)
    exit()

l = 0
max_l = 0
max_l_left = None
#max_l_right = None
for i, s in enumerate(S):
    if l > 0:
        if s == 'o':
            l += 1
            if l > max_l:
                max_l = l
                max_l_left = start
        else:
            l = 0
    elif l == 0:
        if s == 'o':
            l += 1
            if l > max_l:
                max_l = l
                max_l_left = i
            start = i
        else:
            l = 0

print(max_l)