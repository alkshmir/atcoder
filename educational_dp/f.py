s = input()
t = input()

# dp[i][j]をsのi文字目までとtのj文字目までのLCSの長さとする
# 次の3通り考えられる。
# 1. S[i+1] == T[j+1]なら、Sのi+1番目とTのj+1番目を足せばLCSが1伸びるので
# dp[i+1][j+1] = dp[i][j] + 1
# 2. あるいは、Sのi+1番目とTのj番目までを起点に考えて、Tのj+1番目まで考慮しても変わらない場合
# (なぜなら、片方だけ伸ばしてもLCSは増えないため)
# dp[i+1][j+1] = dp[i+1][j]
# 3. 対称に考えると、
# dp[i+1][j+1] = dp[i][j+1]
# 2. 3.は、
# s = abxa,
# t = abyx とすると、
# abxa と abyx のLCSはabxaとabyのLCSまたは、abxとabyxのLCSのどちらかでしょう。
# ということを言っています。

# 文字列比較が重いっぽいので、長さだけ持つことにします。

dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

for i in range(0, len(s)):
    for j in range(0, len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i][j]+1, dp[i+1][j], dp[i][j+1])
            '''
            maxlen = max(len(dp[i][j])+1, len(dp[i+1][j]), len(dp[i][j+1]))
            for lcs in [dp[i][j] + s[i], dp[i+1][j], dp[i][j+1]]:
                if len(lcs) == maxlen:
                    dp[i+1][j+1] = lcs
                    break
            '''
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
            '''
            maxlen = max(len(dp[i+1][j]), len(dp[i][j+1]))
            for lcs in [dp[i+1][j], dp[i][j+1]]:
                if len(lcs) == maxlen:
                    dp[i+1][j+1] = lcs
                    break
            '''

#print(dp[-1][-1])

N = len(s)
M = len(t)
i = N 
j = M 
ans = ''
while i and j:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans += s[i-1]
        i -= 1
        j -= 1
print(ans[::-1])