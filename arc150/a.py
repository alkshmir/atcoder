# 解説読んでわかったけど、そこから何を学べば良い？
# ウインドウをずらしていくという発想
# ウインドウの位置が固定の時、条件を満たすかどうかの判定はウインドウないで完結する
# ウインドウをずらしていくときに差分だけ計算して計算量削減

T = int(input())
for _ in range(T):
    N, K = [int(s) for s in input().split()]
    S = input()
    M = 0
    for s in S:
        if s == "1":
            M += 1
    ones = [0]
    zeros = [0]
    for i in range(K):
        if S[i] == "1":
            ones[0] += 1
        elif S[i] == "0":
            zeros[0] += 1
    cnt = 0
    if ones[-1] == M and zeros[-1] == 0:
        cnt += 1
    for i in range(1, N-K+1):  #i+K-1==N-1
        if S[i+K-1] == "1":
            if S[i-1] == "1":
                ones.append(ones[-1])
                zeros.append(zeros[-1])
            elif S[i-1] == "0":
                ones.append(ones[-1]+1)
                zeros.append(zeros[-1]-1)
            else:
                ones.append(ones[-1]+1)
                zeros.append(zeros[-1])
        elif S[i+K-1] == "0":
            if S[i-1] == "1":
                ones.append(ones[-1]-1)
                zeros.append(zeros[-1]+1)
            elif S[i-1] == "0":
                ones.append(ones[-1])
                zeros.append(zeros[-1])
            else:
                ones.append(ones[-1])
                zeros.append(zeros[-1]+1)
        else:
            if S[i-1] == "1":
                ones.append(ones[-1]-1)
                zeros.append(zeros[-1])
            elif S[i-1] == "0":
                ones.append(ones[-1])
                zeros.append(zeros[-1]-1)
            else:
                ones.append(ones[-1])
                zeros.append(zeros[-1])
        if ones[-1] == M and zeros[-1] == 0:
            cnt += 1
    #print(ones, zeros)
    if cnt == 1:
        print("Yes")
    else:
        print("No")