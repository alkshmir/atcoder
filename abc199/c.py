
N = int(input())
S = [s for s in input()]
inverted = False
Q = int(input())
for _ in range(Q):
    t, a, b = [int(s) for s in input().split()]
    a -= 1
    b -= 1
    if t == 1:
        if inverted:
            if a < N:
                a += N
            else:
                a -= N
            if b < N:
                b += N
            else:
                b -= N
            tmp = S[a]
            S[a] = S[b]
            S[b] = tmp
        else:
            tmp = S[a]
            S[a] = S[b]
            S[b] = tmp
    if t == 2:
        inverted = not inverted

if inverted:
    print("".join(S[N:]+S[:N]))
else:
    print("".join(S))