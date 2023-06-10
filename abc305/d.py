# 睡眠時間の累積和を取っておく
# lとrがAのどこに入るかをみる O(log(N))
# lとrが同じ場所に入る場合、lの左隣が奇数なら0を出力して、偶数ならr-lを出力する
# 以下、l とrは違う場所に入るとする
# lの左隣が奇数2p+1のときはなにもしない、偶数2pの時はA[2p+1]-lを足しておく
# スタートはp+1
# rの左隣が奇数2q-1のときは、r-A[2q]を足しておく、偶数2qのときは何もしない
# ストップは両方q-1
import bisect

N = int(input())
A = [int(s) for s in input().split()]

# 睡眠時間の累積和
slept_time = [0]
for i in range(1, (N-1)//2 + 1):
    slept_time.append(slept_time[-1] + A[2*i] - A[2*i-1])

#print(slept_time)
Q = int(input())
for i in range(Q):
    l, r = [int(s) for s in input().split()]
    l_idx = bisect.bisect_right(A, l)
    r_idx = bisect.bisect_left(A, r)
    #print("idx", l_idx, r_idx)

    if l_idx == r_idx:
        if l_idx%2 == 0:
            print(r-l)
        else:
            print(0)
        continue
    
    ans = 0
    if l_idx%2 == 1:
        # 2p + 1 = l_idx
        p = (l_idx-1)//2
        start = p
    else:
        # 2p = l_idx
        p = l_idx//2
        ans += A[l_idx] - l
        start = p
    #print("ans", ans)

    if r_idx%2 == 0:
        # 2q - 1 = r_idx
        q = (r_idx+1)//2
        stop = q-1
        ans += r-A[r_idx-1]
    else:
        q = r_idx//2
        stop = q
    #print("ans", ans)

    ans += slept_time[stop] - slept_time[start]
    #print(start, stop, ans)
    print(ans)

