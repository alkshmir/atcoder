# Xが99以下なら、Xをそのまま出力する。
# 公差dは-9, -8, ... , 0, 1, 2, ..., 8, 9のどれかだが、
# Xがnけただったとすると、-10 <= d*n <= 10である必要がある
# 従って3桁以上のXを考慮すると-4<=d<=4である
# dが決まっているとき、1の位を決めたらX以上の整数は1つに定まるか、
# 作ることができないかの2択になる。
# 従って、各dで答えの候補を決めてその最小値を答えれば良い
X = int(input())
if X <= 99:
    print(X)
    exit()
ans = 10**18 - 1
for d in range(-4, 5):
    #cand = []
    for s in range(10): # 1の位
        if s == 0 and d == 0:
            continue
        i = 0
        n = s # iけため
        num = s
        while num < X:
            n += d
            if not 0<=n<=9:
                break
            i+=1 
            num += n*10**i
        if num >= X:
            #cand.append(num)
            ans = min(ans, num)
print(ans)