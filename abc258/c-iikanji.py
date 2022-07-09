def main():
    N, Q = input().split()
    N = int(N)
    Q = int(Q)
    S = input()
    query = [input().split() for _ in range(Q)]
    #for i in range(Q):
        #query.append([int(_) for _ in input().split()])
        #query.append(input().split())
    #print(query)

    p = 0
    for q in query:
        x = int(q[1])
        if q[0] == '1':
            #for _ in range(int(q[1])):
            #    last = S[-1]
            #    S = last + S[0:-1]
            #S = S[N-x:] + S[0:-x]
            p += x
            #print(S[N-x:], S[0:-x])
        elif q[0] == '2':
            #print(S[x-1])
            print(S[(x-p-1) % N])

main()