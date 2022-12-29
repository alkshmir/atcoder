# 式の形のまま足していけば、足す回数はXの桁数以下なので、O(logX)でできる
# しかし、50000桁の足し算に非常に時間がかかるためTLEする。
# 大きいけたから見た各桁の累積和を考えると、繰り上がりを考慮しない場合、
# 各桁はその累積和の1の位である。
# 繰り上がりを考慮するときは、各累積和の10の位以上を上位桁に足していけば良い。
# (上位桁がない場合は、新しい要素を追加する)
# この時各要素は大きくとも50000*9=450000以下であり十分に32bit整数に収まる。
# この解法もO(logX)だが定数倍の高速化が見込める。
X = input()
cul = [int(X[0])]
for i in range(1, len(X)):
    cul.append(cul[-1] + int(X[i]))
#print(cul)

ans = []
while(cul):
    #print(cul)
    c = cul.pop()
    ans.append(c%10)
    carry = c // 10
    if carry != 0:
        if cul:
            cul[-1] += carry
        else:
            cul.append(carry)
print(''.join([str(n) for n in ans[::-1]]))