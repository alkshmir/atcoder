# 辞書順
# 文字列の総数は (A+B)!/(A!*B!)なので、最大では60!/(30!*30!)であり、
# 10^17ぐらいなので、O(K)では間に合わない
# しかし、これは64bit整数に収まるので、条件を満たす文字列の数を数えながら
# 条件分岐していくことは可能である
# 一番上の桁がaなのは(A-1+B)!/((A-1)!*B!)個あり、Kがこの値以下であれば一番上の桁はaであり
# そうでなければbである
# また、この時下限を決める(上限を分岐に使用することもできる)
# このようにして上の桁から確定していき、aをi個、bをj個使った時、
# 下限 + (A-i-1+B-j)!/((A-i-1)!*(B-j)!)<Kなら次の桁はb
# なお、i=Aとなれば以降は全てbであり、j=Bとなれば以降全てaである
# 計算量は各桁を確定させるループと階乗計算でO((A+B)^2) 
import math
A, B, K = [int(s) for s in input().split()]
i = 0
j = 0
ans = []
upper = math.factorial(A+B) // math.factorial(A) // math.factorial(B)
lower = 0
for _ in range(A+B):
    if i == A:
        ans.append('b')
        continue
    if j == B:
        ans.append('a')
        continue
    # 上位桁にaをi+1こ、bをjこ使った数の総数
    tmp = math.factorial(A-i-1+B-j) // math.factorial(A-i-1) // math.factorial(B-j)
    if K <= lower + tmp:
        ans.append('a')
        i += 1
        upper = lower + tmp
    else:
        ans.append('b')
        lower = lower + tmp
        j += 1
print(''.join(ans))