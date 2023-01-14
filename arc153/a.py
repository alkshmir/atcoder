# 美しい整数の中で独立な桁は６個でありこれらを順番に数えれば10^6程度になり間に合う

def conv(s: int):
    # sは6けたの自然数
    st = str(s)
    ans = 0
    ans += int(st[0])*10**8 + int(st[0])*10**7
    ans += int(st[1])*10**6
    ans += int(st[2])*10**5
    ans += int(st[3])*10**4 + int(st[3])*10**3
    ans += int(st[4])*10**2 + int(st[4])
    ans += int(st[5])*10**1
    return ans

N = int(input())
t = 100000 + N - 1
print(conv(t))
