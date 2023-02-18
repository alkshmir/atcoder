# 一回の操作で、1の数は2減るか、変わらないか、2増えるかのいずれかなので、操作によって1の数の偶奇は変わらない。
# よって、1の数が奇数の場合はどうやっても全て0にすることはできない。
# 1の数が4以上の時は(1の数)/2が答えである
# 1の数=2の時、1が離れている時は1回。
# 1の数が2でかつ1同士がくっついている時、N>=5なら2回、N=3なら不可能である。
# N=4の時、0011か1100なら2回、0110なら3回

T = int(input())
for _ in range(T):
    n = int(input())
    s = input()
    cnt = 0
    for c in s:
        if c == '1':
            cnt += 1
    if cnt == 2:
        # くっついているかどうかを判定
        for i in range(n):
            if s[i] == '1':
                if s[i+1] == '1':
                    if n >= 5:
                        print(2)
                    elif n == 4:
                        if s == '0011' or s == '1100':
                            print(2)
                        else:
                            print(3)
                    elif n == 3:
                        print(-1)
                else:
                    print(1)
                break

    else:
        if cnt % 2 == 1:
            print(-1)
        else:
            print(cnt//2)
    