
def main():
    h1, h2, h3, w1, w2, w3  = [int(s) for s in input().split()]

    # a b
    # c d

    if h1 + h2 + h3 != w1 + w2 + w3:
        print(0)
        return

    cnt = 0
    for a in range(1, 29):
        for b in range(1, 29):
            for c in range(1, 29):
                for d in range(1, 29):
                    
                    if (
                        1<=h1-a-b<=29 and 
                        1<=h2-c-d<=29 and 
                        1<=w1-a-c<=29 and 
                        1<=w2-b-d<=29 and 
                        1<=w3-h1-h2+a+b+c+d <= 29
                    ):
                        cnt += 1
                        #print(a, b, c, d)
    print(cnt)

if __name__ == "__main__":
    main()