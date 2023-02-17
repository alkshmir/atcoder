# aliceが勝つには、BobのターンでBより小さい玉が残るようにすれば良い
# n < A ならAliceの負け、
# n >= A である時Bより小さくなるように取れれば勝ちでそれ以外は負けである
# n=1からn=Nまで調べるとO(N)かかってしまうので、Aのmoduloを考える
# n < AのものはA-1こある
# n >= A であり、n%A < Bであるようなものは
# B >= A ならば、全て当てはまるので N - (A-1)こある
# B == A - 1とすると、(A-1)*((N-A+1)//A) + K回あるM=N%Aとして K=M+1 if B>M, else B
# B < A の時、一般化すると、B*((N-A+1)//A)+K回 

N, A, B = [int(s) for s in input().split()]
if N < A:
    print(0)
    exit()
if B>=A:
    print(N-A+1)
else:
    m = N%A
    if B>m:
        k = m+1
    else:
        k = B

    print(B*((N-A+1)//A)+k)