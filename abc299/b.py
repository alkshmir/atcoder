N, T = [int(s) for s in input().split()]

C = [int(s) for s in input().split()]
R = [int(s) for s in input().split()]

if T in C:
    alt = [(i, r) for i, (c, r) in enumerate(zip(C, R)) if c == T]
    #print(alt)
    print(sorted(alt, key=lambda x: x[1], reverse=True)[0][0] + 1)
else:
    alt = [(i, r) for i, (c, r) in enumerate(zip(C, R)) if c == C[0]]
    print(sorted(alt, key=lambda x: x[1], reverse=True)[0][0] + 1)
