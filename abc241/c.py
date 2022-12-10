# 縦・横・斜めの各リストを抽出する。(それぞれO(N^2))
# 各リストにて、'.'が2こ、'#'が4個あるような部分列があるかどうかを調べる(O(N))
# リストはO(N)こあるので、部分列を調べるのはO(N^2)でできる。
# よって、最終的にO(N^2)でもとまる。
N = int(input())
S = []
for _ in range(N):
    S.append(input())
tate = []
for i in range(N):
    tate.append([])
    for j in range(N):
        tate[-1].append(S[j][i])

naname_r = []
for i in range((N-1)*2+1):
    naname_r.append([])
    j = max(i-N+1, 0)
    while 0 <= j < N and 0 <= i-j < N:
        naname_r[-1].append(S[i-j][j])
        j += 1

naname_l = []
tmp_s = S[::-1]
for i in range((N-1)*2+1):
    naname_l.append([])
    j = max(i-N+1, 0)
    while 0 <= j < N and 0 <= i-j < N:
        naname_l[-1].append(tmp_s[i-j][j])
        j += 1

for l_2d in [S, tate, naname_r, naname_l]:
    for l in l_2d:
        if len(l) < 6:
            continue
        seg = l[0:6]
        sharps = 0
        for c in seg:
            if c == '#':
                sharps += 1
        if sharps >= 4:
            print("Yes")
            exit()
        for i in range(1, len(l)-5):
            if l[i-1] == '#':
                sharps -= 1
            if l[i+5] == '#':
                sharps += 1
            if sharps >= 4:
                print("Yes")
                exit()
print("No")


