# 演説するとA+B票を得て、演説しないと-A票を得るとして、最終的な得票が正であれば良い
# 全く演説しないときの得票数は-sum(A)で、得票数は演説するごとに2A+B増えるので、
# 2A+Bが多い都市から貪欲に選んでいけば良い
# 得票数が0を超えた時の都市数が答えである

N = int(input())
A = []
B = []
bplus2a = []
for _ in range(N):
    a, b = [int(s) for s in input().split()]
    A.append(a)
    B.append(b)
    bplus2a.append(b+2*a)

votes = -sum(A)
bplus2a.sort(reverse=True)
#print(votes)
#print(bplus2a)
cnt = 0
for v in bplus2a:
    votes += v
    cnt += 1
    if votes > 0:
        break
print(cnt)